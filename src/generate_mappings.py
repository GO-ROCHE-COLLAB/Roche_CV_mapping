#!/usr/bin/env jython -J-Xmx8000m

import sys
import re
import os

# Need to work on balance between the generating script and the module

from mapping_tools import *
from tsv2pdm import *
go = load_ont(sys.argv[1])
manMap = tab('../mapping_tables/', 'manual_mapping.tsv')  # No key row.  Stored as list of dicts.
owlMap = rcd('../mapping_tables/', 'owl_map.tsv', 'RCV_ID') # dict of dicts.
RCV_id_name = {} # Residual perlishness ?
for row in manMap.tab:
	RCV_id_name[row['RCV_ID']]=row['RCV_NAME']

report_path = '../mapping_tables/results/'

for RCV_id in owlMap.rowColDict:
	fname = re.sub(' ', '_', RCV_id_name[RCV_id]) + '_' + RCV_id
	report = ''
	if os.path.isfile(report_path + fname + ".tsv"):
		report = rcd(report_path, fname + ".tsv", 'ID')
	else:
		report = rcd(report_path, 'results_template.tsv', 'ID')
	print "Processing: %s" % RCV_id        
	out = open("../mapping_tables/results/%s.tsv" % fname, "w")
	mo = map_obj(go, RCV_id, manMap.tab, owlMap.rowColDict)
	print "map summary: %s" % mo
	mo.gen_report(report.rowColDict) # Update report object using map object
	out.write(report.print_tab())
	out.close()
	
go.sleep()
