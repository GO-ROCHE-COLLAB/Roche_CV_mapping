#!/usr/bin/env jython -J-Xmx8000m

import sys
import re
import os

# Need to work on balance between the generating script and the module

from mapping_tools import *
from tsv2pdm import *
go = load_ont(sys.argv[1])
manMap = tab('../mapping_tables/', 'manual_mapping.tsv')  # No key row.  Stored as list of dicts.
owlMap = tab('../mapping_tables/', 'owl_map.tsv', 'Roche CV term') # dict of dicts.

report_path = '../mapping_tables/results/'

for rcvt in owlMap.rowColDict:
    fname = re.sub(' ', '_', rcvt)
    report = ''
    if os.path.isfile(report_path + fname + ".tsv"):
        report = tab(report_path, fname + ".tsv", 'ID')
    else:
        report = tab(report_path, 'results_template.tsv', 'ID')
    print "Processing: %s" % rcvt        
    out = open("../mapping_tables/results/%s.tsv" % fname, "w")
    mo = map_obj(go, rcvt, manMap.tab, owlMap.rowColDict)
    print "map summary: %s" % mo
    mo.gen_report(report.rowColDict) # Update report object using map object
    # Now print report.
    for oline in (report.print_tab()):
        out.write(oline + "\n")
    out.close()
go.sleep()
