#!/usr/bin/env python
import sys
import re

def tsv2rowDict(tsv_file_path):
    """Makes a Python data model from as tsv file. The first line is treated as a header. The rest of the table becomes an array of dicts, keyed on the header. (This data model follows the same pattern as dict_cursor making switching between a DB representation and simple TSVs easy as long as TSV headers follow the same pattern as DB column headers.""" 
    tsv_file_obj = open(tsv_file_path, "r")
    hstat = 0
    headers = []
    tab = []
    for line in tsv_file_obj:
        cline = line.rstrip("\n")
        row = {}
        if hstat == 0:
            headers = cline.split("\t")
            hstat = 1
        else:
            content = cline.split("\t")
            i = 0
            for head in headers:
                row[head]=content[i]
                i += 1
            tab.append(row)
    tsv_file_obj.close()
    return tab

def rowDict2ColRowDict(tab_dictList, key_row):
    """Turns a table represented as a list of dicts into a dict of dicts keyed on the contents of a specified key row."""
    row_column_cell = {}
    
    for d in tab_dictList:
        row_key = d[key_row]
        for column_key in d:
            if row_key not in row_column_cell:
                row_column_cell[row_key] = {}
            row_column_cell[row_key][column_key] = d[column_key]
    return row_column_cell
