#!/usr/bin/env python
import sys
import re
import warnings

# Maybe use existing util rather than reinventing the wheel, e.g. https://github.com/brendano/tsvutils ?
            

class tab:
    ### A rather clunky implementation - tab has 2 states: RD and RCD.  RD is used when no key column is specified or when the specified key column is invalid.  It stores the tab as a list of dicts keyed on column.  RCD is used when a valid column key is specified.  It stores the tab as a dict of dicts - [row][column].  
    """ A class for making table objects from TSV files with headers and for printing TSVs from the results."""
    headers = [] # List used to preserve order of columns
    key_column = '' # The header name of the row key column, if any.
    # Store as colDict hash.
    file_name = ''
    tab = [] # default stored as list of dicts keyed on row.
    rowColDict = {}
    _typ = '' # Type may be RCD (Row dict of column dict) or RD (a list of dicts keyed on column)

    def __str__(self):
        if self._typ == 'RD':
            return "file: %s; type: %s; length: %d" % (self.file_name, self._typ, len(self.tab)-1)
        elif self._typ == 'RCD':
            return "file: %s; type: %s; key_column: %s; length: %d" % (self.file_name, self._typ, self.key_column, len(self.rowColDict.keys())-1)

    
    def __init__(self, path, file_name, key_column = ''):
        """Read in file. First arg is path to file, minus file name (not stored in object), second arg is file name, third arg is the column to be used as a key"""
        self.file_name = file_name
        self.key_column = key_column
        self._typ = '' # Type may be RCD (Row dict of column dict) or RD (a list of dicts keyed on column)
        self.tab = [] # If no valid key column, this stores table data as list of dicts keyed on column. Otherwise this is an empty list.
        self.rowColDict = {} # If there is a valid key column - data is store here as a dict of dicts - [row][column]
        tsv_file = open(path + file_name, "r") 
        hstat = 0
        for line in tsv_file:
            cline = line.rstrip("\n")
            if hstat == 0:
                self.headers = cline.split("\t")
                hstat = 1
            else:
                row = {}
                content = cline.split("\t")
                i = 0
                for head in self.headers:
                    row[head]=content[i]
                    i += 1
                self.tab.append(row)
        if self.key_column:
            if self.key_column_check():
                self.genRowColDict()
                self._typ = 'RCD' # Using convention for private attribute
                self.tab = [] # Zero out tab.  Master is now RCD.
            else:
                self._typ = 'RD'
        else:
            self._typ = 'RD'
        tsv_file.close()
    
    def key_column_check(self):
        """A method to check that the key column is in header and is a uniq'd list"""
        # is key column in header?
        if self.key_column not in self.headers:
            warnings.warn("The specified key column: %s is not in the header of %s!" % (self.key_column, self.file_name))
            self.key_column = ''
            return False
        # is key column content uniq'd?
        else:
            column = []
            for row in self.tab:
                column.append(row[self.key_column])
            if len(column) > len(set(column)):
                warnings.warn("The key column contains duplicate keys!")
                return False
            else:
                return True

    def getRowDict(self):
        return self.tab
    
    def genRowColDict(self):
        """Turns a table represented as a list of dicts into a dict of dicts keyed on the contents of a specified key row."""
        # only roll if there is a key column
        if self.key_column:
            for d in self.tab:
                row_key = d[self.key_column]
                for column_key in d:
                    if row_key not in self.rowColDict:
                        self.rowColDict[row_key] = {} # initialise dict for row
                    self.rowColDict[row_key][column_key] = d[column_key] # populate row dict
        else:
            warnings.warn("Can't generate RowColDict without valid keyColumn")

    def getRowCollDict(self):
        return self.rowDict
        
    def print_tab(self):
        out_tab = []
        if self._typ == 'RCD':
            # populate tab for the purpose of printing
            out_tab = self.rowColDict.values()
        elif self._typ == 'RD':
            out_tab = self.tab
        out = []
        h2 = self.headers[:] 
        out.append(self._row_gen(h2))
        for row in out_tab:
            outrow_list = []
            for h in self.headers:
                outrow_list.append(row[h])
            out.append(self._row_gen(outrow_list))
        return out

    def _row_gen(self, rowList):
        rowList.reverse() # So popping works from the right end, in the absence of shift method...
        out = ''
        while rowList:
            out += unicode(rowList.pop())  # everything must become a unicode string in the output.  
            if rowList:
                out += "\t"
        return out

    
    
