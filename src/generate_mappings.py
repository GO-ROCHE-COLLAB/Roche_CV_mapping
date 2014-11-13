#!/usr/bin/env jython -J-Xmx8000m

import sys
import re
import os
import warnings


# Need to work on balance between the generating script and the module

#  TODO: Add code to generate full mapping table.  This can be derived from results tables + ticket info without a further reasoner run.
## Spec: Include combined manual & auto mappings that are not blacklists from results files for while a ticket exists with label: mapping_complete. 


# Rather scrappy, Perlish procedural code for generating mappings.

"""Reads owl_map and uses it to automatically populate RCV classes.  
Compares these to manual mappings. Prints a results summary and results tables.
Ontology to use must be specified as argv[1] when runnning this script."""

from mapping_tools import (map_obj, load_ont, mappingTabs)
from tsv2pdm import tab, rcd


go = load_ont(sys.argv[1])


manMap = tab('../mapping_tables/', 'manual_mapping.tsv')  # No key row.  Stored as list of dicts.
owlMap = rcd('../mapping_tables/', 'owl_map.tsv', 'RCV_ID') # dict of dicts.
RCV = rcd('../mapping_tables/', 'RocheCV_def.tsv', 'RCV_ID') # dict of dicts.

mapping_tabs = mappingTabs(manMap.tab, owlMap.rowColDict, RCV.rowColDict, go) 
# ...Hmmm - would give much more flexibility if passed objects rather than data structures.

manMap_updated = open('../mapping_tables/manual_mapping.tsv', "w")
manMap_updated.write(manMap.print_tab(sort_keys=('RCV_ID',)))
manMap_updated.close()

RCV_id_name = {} # Residual perlishness ?
for row in manMap.tab:
	RCV_id_name[row['RCV_ID']]=row['RCV_NAME']

report_path = '../mapping_tables/results/'



# TODO - add check for integrity of existing results files.  This can be automated from the results template.

report_dir_files = os.listdir(report_path)

report_template = tab(report_path, "results_template.tsv")

class BadlyFormedResultFile(Exception):
	def __init__(self, f):
		self.f = f
		warnings.warn("Badly formed results file %s" % f)

for f in report_dir_files:
	if re.search("RCV_\d{6}.tsv", f):
		table = tab(report_path, f)
		try:
			assert (table.headers == report_template.headers)
		except:
			BadlyFormedResultFile(f)


summary = "## A summary of the current results, including links to results files & issues.\n\n"

# TODO - sort summary output on issue stat and then alphanumerically. 

for RCV_id, rd in owlMap.rowColDict.items():
	if not mapping_tabs.rcv[RCV_id]['STATUS']:
		warnings.warn("%s is in owl_map but is obsolete" % RCV_id) # Need to write this to owl_map so know not to bother writing mapping!
	else:
		# Skip cases where class expression marked as missing or preliminary    	
		if re.match("\?.*", rd['Applied pattern']):
			if rd["Notes"]:
				summary += "#### %s %s\n" % (RCV_id_name[RCV_id], RCV_id)
				summary += "* Notes: %s\n" % rd["Notes"]
				summary += "* Results: N/A Job not run. Specification marked as preliminary or missing.\n\n"
			continue
		else:
			summary += "#### %s %s\n" % (RCV_id_name[RCV_id], RCV_id)
			summary += "* Key class: [%s](http://www.ebi.ac.uk/ontology-lookup/?termId=%s)\n" % (rd["Key Class Name"], re.sub('_', ':', rd["Key Class ID"]))
			summary += "* Pattern: [%s](../../patterns/%s.md)\n" % (rd["Applied pattern"], rd["Applied pattern"])
	
			fname = re.sub(' ', '_', RCV_id_name[RCV_id]) + '_' + RCV_id
			report = ''
			if os.path.isfile(report_path + fname + ".tsv"):
				report = rcd(report_path, fname + ".tsv", 'ID') # why not use tab rather than rcd?
			else:
				report = rcd(report_path, 'results_template.tsv', 'ID') # default to template if not already present.
			print "Processing: %s" % RCV_id       
			mo = map_obj(RCV_id, mapping_tabs, "../patterns/")
			summary += "* Definition: %s\n" %	mo.appl_pattern.definition
			print "map summary: %s\n" % mo
			summary += "* map summary: %s\n" % mo
			if rd["Notes"]:
				summary += "* Notes: %s\n" % rd["Notes"]
			summary += "* [Results](%s.tsv)\n" % fname
			summary += "* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/%s)\n" % rd['issue']
			summary += "* Status: %s\n\n" % rd['issue_state']
	
			# Pass existing report to map object, and update using gen_report method # Confusing way to work?  
			mo.gen_report(report.rowColDict)
			# print, sorting on manual followed by auto.  Use reverse sort order = True
			out = report.print_tab(("manual","auto", "name"), True)
	
			# only print a new results file if it has anything in it.
			if out:
					outfile = open("../mapping_tables/results/%s.tsv" % fname, "w")
					outfile.write(out) 
					outfile.close()
	

summary_file = open("../mapping_tables/results/results_summary.md", "w")
summary_file.write(summary)
summary_file.close()
combined_results_file = open("../mapping_tables/results/combined_results.tsv", "w")
cr_table = mapping_tabs.combined_results.print_tab(sort_keys=('RCV_ID', 'GO_NAME'))
combined_results_file.write(cr_table)
combined_results_file.close()
go.sleep()