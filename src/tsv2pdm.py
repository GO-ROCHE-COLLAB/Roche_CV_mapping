#!/usr/bin/env python
import sys
import re
import warnings

# Maybe use existing util rather than reinventing the wheel, e.g. https://github.com/brendano/tsvutils ?

# Refactoring plan: split class into super (RC) and sub (RCD)


class tab(object):
    """Stores a tsv file as a list of dicts keyed on column header. Users should directly manipulate the tab attribute, which contains this datastructure. The method print tab returns the table as a list of strings for printing."""

    def __str__(self):
        return "file: %s; type = simple table; length: %d" % (self.file_name, len(self.tab)-1)
    
    def __init__(self, path, file_name, key_column = ''):
        """Read in file. First arg is path to file, minus file name (not stored in object), second arg is file name, third arg is the column to be used as a key"""
        self.file_name = file_name
        self.key_column = key_column
        self.tab = [] # list of dicts, keyed on column.
        self.rowColDict = {} #  dict of dicts - [row][column]
        self.headers = [] # declare headers as a list
        self.parse_tsv(path, file_name)  # 

    def parse_tsv(self, path, file_name):
        tsv_file = open(path + file_name, "r")
        hstat = 0
        for line in tsv_file:
            cline = line.rstrip("\n")
            if hstat == 0:
                self.headers.extend(cline.split("\t"))
                hstat = 1
            else:
                row = {}
                content = cline.split("\t")
                i = 0
                for head in self.headers:
                    row[head]=content[i]
                    i += 1
                self.tab.append(row)
        tsv_file.close()
        
    def print_tab(self):
        out_tab = []
        # This is ugly - testing membership of child class in parent class. But acceptable I think, given the this is unlikely to be extended and that the alternatives - redundant data structures or a class specific print method, are more likely to cause data processing problems.
        if isinstance(self, rcd):
            # populate tab for the purpose of printing
            out_tab = self.rowColDict.values()
        else:
            out_tab = self.tab
        out = []
        out.append('\t'.join(self.headers))
        for row in out_tab:
            outrow = []
            for h in self.headers:
                outrow.append(row[h])
            out.append('\t'.join(map(unicode, outrow)))  # All content of list to unicode, then joined with a tab, then appended to output.
        return '\n'.join(out)

    
class rcd(tab):
    """A class for making tables with a key column.  The contents of this column must be uniq'd. The table is stored in the attribute rowColDict, which stores the tab as a dict of dicts - [row][column]."""
    def __str__(self):
        return "file: %s; type: row column dict; key_column: %s; length: %d" % (self.file_name, self.key_column, len(self.rowColDict.keys())-1)
        
    def __init__(self, path, file_name, key_column):
        self.file_name = file_name
        self.key_column = key_column
        self.tab = [] # list of dicts keyed on column
        self.rowColDict = {} # dict of dicts - [row][column]
        self.headers = [] # declare headers as a list
        self.parse_tsv(path, file_name)
        if self.key_column_check():
            self.genRowColDict()
            
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
            self.tab = [] # Zero out tab.  Master is now RCD.  # This seems a bit dodgy...
        else:
            warnings.warn("Can't generate RowColDict without valid keyColumn") # Make this into a fatal warning?
        
    def key_column_check(self):
        """A method to check that the key column is in header and is a uniq'd list"""
        # is key column in header?
        if self.key_column not in self.headers:
            warnings.warn("The specified key column: %s is not in the header of %s!" % (self.key_column, self.file_name)) # Make this into a fatal warning?
            self.key_column = ''
            return False
        # is key column content uniq'd?
        else:
            column = []
            for row in self.tab:
                column.append(row[self.key_column])
            if len(column) > len(set(column)):
                warnings.warn("The key column contains duplicate keys!") # Make this into a fatal warning?
                return False
            else:
                return True
