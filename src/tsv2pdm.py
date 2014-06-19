#!/usr/bin/env python
import sys
import re
import warnings

# Maybe use existing util rather than reinventing the wheel, e.g. https://github.com/brendano/tsvutils ?
            

class tab:
    """ A class for making table objects from TSV files with headers."""
    headers = [] # List used to preserve order of columns
    key_column = '' # The header name of the row key column, if any.
    # Store as colDict hash.
    file_name = ''
    tab = [] # default stored as list of dicts keyed on row.

    def __str__(self):
        return "file: %s; key_colum: %s; length: %d" % (self.file_name, self.key_column, len(self.tab)-1)
    
    def read_tab(self, path, file_name, key_column = ''):
        """Read in file. First arg is path to file, minus file name (not stored in object), second arg is file name, third arg is the column to be used as a key"""
        self.file_name = file_name
        self.key_column = key_column
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
            self.key_column_check()
        tsv_file.close()
    
    def key_column_check(self):
        """A method to check that the key column is in header and is a uniq'd list"""
        # is key column in header?
        if self.key_column not in self.headers:
            warnings.warn("The specified key column is not in the header!")
            self.key_column = ''
        # is key column content uniq'd?
        else:
            column = []
            for row in self.tab:
                column.append(row[self.key_column])
            if len(column) > len(set(column)):
                warnings.warn("The key column contains duplicate keys!")

    def getRowDict(self):
        return self.tab
    
    def getRowColDict(self):
        """Turns a table represented as a list of dicts into a dict of dicts keyed on the contents of a specified key row."""
        if not self.row
        row_column_cell = {}
        for d in self.tab:
            row_key = d[self.key_column]
            for column_key in d:
                if row_key not in row_column_cell:
                    row_column_cell[row_key] = {}
                row_column_cell[row_key][column_key] = d[column_key]
        return row_column_cell
    
    def print_tab(self):
        out = []
        h2 = [] 
        h2.extend(self.headers) # surely there is a better way to do this?!
        out.append(self.row_gen(h2))
        for row in self.tab:
            outrow_list = []
            for h in self.headers:
                outrow_list.append(row[h])
            out.append(self.row_gen(outrow_list))
        return out

    def row_gen(self, rowList):
        rowList.reverse() # So popping works from the right end, in the absence of shift method...
        out = ''
        while rowList:
            out += rowList.pop()
            if rowList:
                out += "\t"
        return out

    
    
