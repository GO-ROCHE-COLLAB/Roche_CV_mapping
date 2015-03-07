#!/usr/bin/env python
import warnings
import operator

# Maybe use existing util rather than reinventing the wheel, e.g. https://github.com/brendano/tsvutils ?


class tab(object):
    """Stores a tsv file as a list of dicts keyed on column header. 
    Users should directly manipulate the tab attribute, which contains this datastructure. 
    The method print_tab returns the table as a list of strings for printing."""

    def __str__(self):
        return "file: %s; type = simple table; length: %d" % (self.file_name, len(self.tab)-1)
    
    def __init__(self, path = '', file_name = '', key_column = '', headers = []):
        """Read in file. 
        First arg, path, is path to file, minus file name (not stored in object)
        Second arg , file_name, is file name.
        Third arg, key_column, is a key column to be used for rolling rowColDict.
        All args are optional, entering no args produces a blank object 
        and throws an non-fatal warning. The preferred way of creating an empty table is to specify
        headers or headers + key_column in the constructor."""
        self.file_name = file_name
        self.path = path
        self.key_column = key_column
        self.tab = [] # list of dicts, keyed on column.
        self.rowColDict = {} #  dict of dicts - [row][column]

        if path and file_name:
            if headers:
                warnings.warn("Ignoring specified headers in favor of those in table.")
            self.headers = []
            self.parse_tsv(path, file_name)  # 
        elif headers:
            self.headers = headers
        else:
            warnings.warn("Warning: Creating blank tab object")
    
    def validate(self):
        for row in self.tab:
            if not self.validate_row(row):
                return False
            
    def validate_row(self, row):
        for k in row.keys():
            if k not in self.headers:
                warnings.warn("Unknown column header %s. Valid headers are %s." % (k, str(self.headers)))
                return False
            else:
                return True
        
                        
    def _parse_tsv(self, path, file_name):
        tsv_file = open(path + file_name, "rU")
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
        
    def parse_tsv(self, path, file_name):
        self._parse_tsv(path, file_name)
        
    def print_tab(self, sort_keys=(), reverse=False):
        """Returns table as a string.  Optionally specify a tuple of columns to sort as sort_keys.
        Default normal sort order.  Optionally specify reverse as a boolean (applies to all columns)."""
        #Creating to allow overide that does other stuff before calling _print_tab
        return self._print_tab(sort_keys, reverse)
        
    def _print_tab(self, sort_keys=(), reverse=False):
        """Returns table as a string.  Optionally specify a tuple of columns to sort as sort_keys.
        Default normal sort order.  Optionally specify reverse as a boolean (applies to all columns)."""
        if sort_keys:
            self.sort_tab(sort_keys, reverse)
        out = []
        out.append('\t'.join(self.headers))
        for row in self.tab:
            outrow = []
            for h in self.headers:
                outrow.append(row[h])
            out.append('\t'.join(map(unicode, outrow)))  # All content of list to unicode, then joined with a tab, then appended to output.
        return '\n'.join(out)
    
    def sort_tab(self, sort_keys=(), reverse=False):
        # For how this works, see http://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        self.tab.sort(key = operator.itemgetter(*sort_keys), reverse=reverse) # Note. * operator unpacks tuple.
        
    def save_tab(self, path = '', file_name = '', sort_keys = (), reverse = False):
        if not path:
            path = self.path
        if not file_name:
            file_name = self.file_name
        out = open(path+file_name, 'w')
        out.write(self.print_tab(sort_keys, reverse))
        out.close()
    
    def _append_column(self, cname, content=''):
        """PRIVATE METHOD. EXTERNAL USE MAY BE UNSAFE!
        Append a column called cname to the table.
        """
        self.headers.append(cname)
        for r in self.tab:
            r[cname] = content # default content empty string
            
    def append_column(self, cname, content = ''):
        """Append a column called cname to the table.
        Optionally define default content of column.
        (if unspecified, this = empty string.)"""
        self._append_column(cname, content)

class rcd(tab):
    """A class for making tables with a key column. 
     The contents of this column must be uniq'd. 
     Attributes (instance level):
       - rowColDict - Primary data storage
                    =  table as a dict of dicts - [row][column].
       - headers - Table headers, stored as a list.
    """
    
    # __init__ inherited from tab
       
    def __str__(self):
        return "file: %s; type: row column dict; key_column: %s; length: %d" % (self.file_name, self.key_column, len(self.rowColDict.keys())-1)
        
    def parse_tsv(self, path, file_name):
        """Parses tsv file into self.rowColumnDict"""
        self._parse_tsv(path, file_name)
        if self.key_column_check():
            self.genRowColDict()
        
    def genRowColDict(self):
        """Turns a table represented as a list of dicts into a dict of dicts 
        keyed on the contents of self.key_column."""
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
            
    def print_tab(self, sort_keys=(), reverse=False):
        # Overriding method
        """Returns table as a string.  Optionally specify a tuple of columns to sort as sort_keys.
        Default normal sort order.  Optionally specify reverse as a boolean (applies to all columns)."""
        self.tab = self.rowColDict.values()
        out = self._print_tab(sort_keys, reverse)
        self.tab = []  # Blanking out as this is not primary store for datamodel.
        return out
    
    def append_column(self, cname, content = ''):
        """Append a column called cname to the table"""
        # Overides method on tab. Result is the same, but made safe for rcd
        self.tab = self.rowColDict.values()
        self._append_column(cname, content)
        self.genRowColDict()
        self.tab = [] # Blanking out as this is not primary store for datamodel.
        
        
            
