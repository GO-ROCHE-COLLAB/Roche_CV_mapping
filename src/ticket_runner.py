#!/usr/bin/env python

import re
from github_tools import issueConn
from tsv2pdm import rcd

"""Generates a set of proforma tickets using owl_map.tsv 
for entries in which the pattern field does not begin with a '?'
and for which there is not currently ticket following the standard name pattern.
Writes ticket URL and state back to owl_map
"""


ic = issueConn('GO-ROCHE-COLLAB', 'Roche_CV_mapping', 'dosumis')
t = ic.set_credentials_from_cl()

owlMap = rcd('../mapping_tables/', 'owl_map.tsv', 'RCV_ID') # dict of dicts.
for RCV_id, rd in owlMap.rowColDict.items():
    if not re.match("\?.*", rd['Applied pattern']):
        issue = ic.ticket_exists("Review %s %s" % (rd['RCV_NAME'], RCV_id)) # Hack-yness alert: tracking on ticket name!
        if not issue:
            issue = ic.create_standard_review_ticket(RCV_id, rd['RCV_NAME'])
        owlMap.rowColDict[RCV_id]['issue'] = issue['number']
        owlMap.rowColDict[RCV_id]['issue_state'] = issue['state']
        
owlMap_file = open("../mapping_tables/owl_map.tsv", "w")
owlMap_file.write(owlMap.print_tab(sort_keys=('issue_state', 'RCV_ID')))
owlMap_file.close()