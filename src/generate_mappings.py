#!/usr/bin/env jython -J-Xmx8000m

import sys
import re
import os
import warnings

# Need to work on balance between the generating script and the module

"""Reads owl_map and uses it to automatically populate RCV classes.  
Compares these to manual mappings. Prints a results summary and results tables.
Ontology to use must be specified as argv[1] when runnning this script."""

from mapping_tools import *
from tsv2pdm import tab, rcd
manMap = tab('../mapping_tables/', 'manual_mapping.tsv')  # No key row.  Stored as list of dicts.
owlMap = rcd('../mapping_tables/', 'owl_map.tsv', 'RCV_ID') # dict of dicts.
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


# Need to write summary generator again.  Seem to have misplaced code!

go = load_ont(sys.argv[1])


summary = "## A summary of the current results, including links to results files.\n\n"




for RCV_id, rd in owlMap.rowColDict.items():
	# Skip cases where class expression marked as missing or preliminary      
	if re.match("\?.*", rd['class expression IDs']):
		if rd["Notes"]:
			summary += "#### %s %s\n" % (RCV_id_name[RCV_id], RCV_id)
			summary += "* Notes: %s\n" % rd["Notes"]
			summary += "* Results: N/A Job not run. Specification marked as preliminary or missing.\n\n"
		continue
	else:
		summary += "#### %s %s\n" % (RCV_id_name[RCV_id], RCV_id)
		summary += "* Key class: [%s](http://purl.obolibrary.org/obo/%s)\n" % (rd["Key Class name"], rd["Key Class ID"])
		summary += "* Pattern: [%s](../../patterns/%s.md)\n" % (rd["Applied pattern"], rd["Applied pattern"])
		fname = re.sub(' ', '_', RCV_id_name[RCV_id]) + '_' + RCV_id
		report = ''
		if os.path.isfile(report_path + fname + ".tsv"):
			report = rcd(report_path, fname + ".tsv", 'ID') # why not use tab rather than rcd?
		else:
			report = rcd(report_path, 'results_template.tsv', 'ID')
		print "Processing: %s" % RCV_id       
		out = open("../mapping_tables/results/%s.tsv" % fname, "w")
		mo = map_obj(go, RCV_id, manMap.tab, owlMap.rowColDict)
		print "map summary: %s\n" % mo
		summary += "* map summary: %s\n" % mo
		if rd["Notes"]:
			summary += "* Notes: %s\n" % rd["Notes"]
		summary += "* [Results](%s.tsv)\n\n" % fname
		# Update report object using map object.  # Confusing way to work?  
		mo.gen_report(report.rowColDict)
		# print, sorting on manual followed by auto.  Use reverse sort order = True
		out.write(report.print_tab(("manual","auto"), True)) 
		out.close()

summary_file = open("../mapping_tables/results/results_summary.md", "w+")
summary_file.write(summary)
summary_file.close()
go.sleep()
