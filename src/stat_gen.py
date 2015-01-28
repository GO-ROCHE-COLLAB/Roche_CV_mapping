# Script to generate stats on mapping
# Number of classes where auto mapping is sufficient

from tsv2pdm import tab, rcd
from glob import glob1
import re
from numpy import average, median, sum, round

    # TODO - hook, directly or indirectly, into the ticket system.  Could pull from owl_map.

results = glob1("../mapping_tables/results/", "*_RCV_*.tsv")

stats = tab(key_column = "RCV_ID", headers = ['RCV_ID', 'RCV_name', 
                                              'Auto sufficient', 'Manual only',
                                               'Auto only', 'Manual blacklist',
                                               'Auto blacklist'])

owl_map = rcd(path = "../mapping_tables/", file_name = "owl_map.tsv", key_column = 'RCV_ID' )

total_sufficient_maps = 0

# Lists for doing basic statistical analysis of results
# Sure this could be done more elegantly with list comps on tab, but still...

Auto_sufficient = []
Manual_only = []
Auto_only = []
Auto_blacklist = []
Manual_blacklist = []


for result in results:
    rtab = tab(path = "../mapping_tables/results/", file_name = result)   
    stat = 1
    extra = 0
    decomp = re.search("^(.+)_(RCV_\d{6}).tsv", result)
    RCV_ID = decomp.group(2)
    # Only add completed mappings to table
    if not owl_map.rowColDict[RCV_ID]['issue_state'] == 'closed - mapping completed':
        continue
    row = {}
    row['RCV_ID'] = RCV_ID
    row['RCV_name'] = re.sub("_", " ", decomp.group(1))
    row['Auto only'] = 0
    row['Auto sufficient'] = 1  # Assumed to be sufficient until row found indicating otherwise
    row['Manual only'] = 0
    row['Auto blacklist'] = 0
    row['Manual blacklist'] = 0
    
    for irow in rtab.tab:
        # Test if auto-mapping finds all non-blacklisted manual annotations.
        if int(irow['manual']) and not int(irow['auto']) and not int(irow['blacklisted']):
            row['Auto sufficient'] = 0
            row['Manual only'] += 1
        if int(irow['auto']) and not int(irow['manual']):
            row['Auto only'] += 1
        if int(irow['auto']) and int(irow['blacklisted']):
            row['Auto blacklist'] += 1
        if int(irow['manual']) and int(irow['blacklisted']) and not int(irow['is_obsolete']):
            row['Manual blacklist'] += 1
    Auto_sufficient.append(row['Auto sufficient'])
    Manual_only.append(row['Manual only'])
    Auto_only.append(row['Auto only'])
    Auto_blacklist.append(row['Auto blacklist'])
    Manual_blacklist.append(row['Manual blacklist'])         
    stats.validate_row(row)
    stats.tab.append(row)
    
# some summary stats.  Hmmm - really should use a function here:

stats.tab.append(
        {'RCV_ID' : 'SUM', 
        'RCV_name' : len(Auto_sufficient),
        'Auto sufficient' : sum(Auto_sufficient),
        'Manual only' : sum(Manual_only),
        'Auto only' : sum(Auto_only),
        'Manual blacklist' : sum(Auto_blacklist),
        'Auto blacklist' : sum(Manual_blacklist)  
        })       

stats.tab.append(
            {'RCV_ID' : 'AVERAGE',
            'RCV_name' : '-',
            'Auto sufficient' : '-',
            'Manual only' : round(average(Manual_only), 2),
            'Auto only' : round(average(Auto_only), 2),
            'Manual blacklist' : round(average(Auto_blacklist),2),
            'Auto blacklist' : round(average(Manual_blacklist), 2)  
            })

stats.tab.append(
            { 'RCV_ID' : 'MEDIAN',
            'RCV_name' : '',
            'Auto sufficient' : '-',
            'Manual only' : round(median(Manual_only), 2),
            'Auto only' : round(median(Auto_only), 2),
            'Manual blacklist' : round(median(Auto_blacklist), 4),
            'Auto blacklist' : round(median(Manual_blacklist),4)  
            })
    
    
#summary = '# Summary of results of automated mapping\n\n' \
#            '__Number of sufficient mappings__: %d' % total_sufficient_maps

outfile_stats = open("../mapping_tables/results/stats.tsv", "w")
#outfile_summary = open("../mapping_tables/results/stats_summary.md", "w")
outfile_stats.write(stats.print_tab())
outfile_stats.close()
#outfile_summary.close()

        
            
            
        

