#!/usr/bin/env/ jython -J-Xmx8000m
from mapping_tools import *
from tsv2pdm import *
go = load_ont('file:///repos/go_trunk_ont/extensions/go-plus.owl')
manMap = tsv2colDict('../mapping_tables/manual_mapping.tsv')
owlMap = rowDict2ColRowDict(tsv2colDict('../mapping_tables/owl_map.tsv'), 'Roche CV term')
for line in manMap:
    rcvt = line['Roche CV term']
    if rcvt in owlMap:
        out = open("../mapping_files/results/%s.tsv" % rcvt, "w")
        mo = map_obj()
        mo.init(go, rcvt, manMap, owlMap)
        out = mo.print_report()
go.sleep()
