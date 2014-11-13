#!/usr/bin/env python

import re
from github_tools import issueConn
from tsv2pdm import rcd, tab
import glob
import warnings

"""Generates a set of proforma tickets using owl_map.tsv 
for entries in which the pattern field does not begin with a '?'
and for which there is not currently ticket following the standard name pattern.
Writes ticket number and state back to owl_map;
If mapping complete, updates RCV master file to record mapping_complete = 1
"""

ic = issueConn('GO-ROCHE-COLLAB', 'Roche_CV_mapping', 'dosumis')
owlMap = rcd('../mapping_tables/', 'owl_map.tsv', 'RCV_ID') # dict of dicts.
RCV = rcd('../mapping_tables/', 'owl_map.tsv', 'RCV_ID')

for RCV_id, rd in owlMap.rowColDict.items():
    if not re.match("\?.*", rd['Applied pattern']):
        ticket_name = "Review %s %s" % (rd['RCV_NAME'], RCV_id)
        issue = ''
        issues = ic.ticket_exists(ticket_name, {'mapping_review'})     
        if not issues:
            issue = ic.create_standard_review_ticket(RCV_id, rd['RCV_NAME'])
        if len(issues) > 1:
            warnings.warn("Multiple tickets exist with the name '%s' and the label 'mapping_review' %s." % ticket_name)
            continue
        issue = issues[0]
        if issue['status'] == 'closed':
            if 'mapping_complete' in issues['labels']:
                RCV.rowColDict[RCV_id]['mapping_complete'] = 1
        owlMap.rowColDict[RCV_id]['issue'] = issue['number']
        owlMap.rowColDict[RCV_id]['issue_state'] = issue['state']
owlMap_file = open("../mapping_tables/owl_map.tsv", "w")
owlMap_file.write(owlMap.print_tab(sort_keys=('issue_state', 'RCV_ID')))
owlMap_file.close()



