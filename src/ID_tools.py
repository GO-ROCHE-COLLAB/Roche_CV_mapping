#!/usr/bin/env python
import warnings

class ontId:
    def __str__(self):
        return "IDP: %s; accession length: %d; Separator: '%s'; number of IDs in dict: %d" % (self.idp, self.length, self.sep, len(self.id_name.keys()))
    def __init__(self, idp, length, id_name, sep = '_'):
        """ARG1: ID prefix (string), ARG3, length of numeric portion ID, ARG4 an id:name hash"""
        # if type(length) not integer  # How to properly add type checks here?
        # if type(id_name) not dict  # How to properly add type checks here?
        self.idp = idp
        self.length = length
        self.id_name = id_name
        self.sep = sep
        self.accession = 1 # default starting accession for init.
        self.name_id = dict((v,k) for k, v in id_name.iteritems())
    def gen_id(self, name):
        k = self._gen_key ()
        while k in self.id_name:
            self.accession += 1
            k = self._gen_key()
        self.id_name[k]=name
        self.name_id[name] = k
        return k #
    def _gen_key(self):
        dl = len(str(self.accession)) # coerce int to string.
        k = self.idp+self.sep+(self.length - dl)*'0'+str(self.accession)
        return k




def test_gen_id():
    # make a dict

    id_name = {}
    id_name['HSNT:00000001'] = 'head'
    id_name['HSNT:00000002'] = 'shoulders'
    id_name['HSNT:00000003']= 'knees'

    hsnt = ontId('HSNT', 8, id_name, ':')

    # Generate ID for new term 'toes'
    k = hsnt.gen_id('toes')
    # Change these to warnings:
    if (k == 'HSNT:00000004') & (hsnt.id_name[k] == 'toes'):
        return True
    else: 
        warnings.warn('gen_id is broken')
        return False


test_gen_id()
