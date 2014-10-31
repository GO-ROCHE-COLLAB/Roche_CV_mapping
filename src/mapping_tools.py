#!/usr/bin/env jython -J-Xmx8000m
from uk.ac.ebi.brain.core import Brain
from owltools.graph import OWLGraphWrapper
import re
from pattern import gen_applied_pattern_from_json
import warnings
from obs_check import manual_map
# TODO - switch from Brain to owltools

def load_ont(url):
	ont = Brain()
	ont.learn(url)
	return ont


# def brain2graphWrapper(ont):
# 	onto = ont.getOntology()
# 	return OWLGraphWrapper(onto)

#def roll_basic_pattern (key_class):
#	return "(has_participant some) %s or (regulates some (has_particpant some %s))" % (key_class, key_class) # If using this pattern, will need OWLtools/HermiT.
class mappingTabs():
	def __init__(self, manual_map, owl_map, go):
		self.manual_map = manual_map
		self.owl_map = owl_map
		self.go = go
		self.update_manual_map_obs_stat()
	
	def RCV_id_2_owlMap(self, RCV_id):
		return self.owl_map.rcd[RCV_id]
		
	def RCV_id_2_man_map(self, RCV_id):
		out = []
		for i in self.manual_map.tab:
			if i['RCV_id'] == RCV_id:
				out.append(i)
		return out
	
	def update_manual_map_obs_stat(self):
		"""Does what is says on the tin"""
		# Right now jsut warns.  Perhaps add extra column to manual map?
		gonto = self.go.getOntology()
		gogw = OWLGraphWrapper(gonto)
		for c in self.manual_map.tab:
			obo_id = re.sub('_', ':', c['GO_ID']) # Hard to believe this is necessary!
			clazo = gogw.getOWLClassByIdentifier(obo_id)
			if gogw.isObsolete(clazo):
				warnings.warn("Obsolete class: %s"  %  c['GO_ID'])
				c['STATUS'] = 0

class map_obj:
	# Should this work on ids or names?  Seems wasteful to store both.
	def __str__(self):
		return "Roche_cvt: %s; class_expression %s; manual_list_count %d, generated_list_count %d" % (self.RCV_id, self.class_expression, len(self.manual_list), len(self.generated_list))
	def __init__ (self, RCV_id, mapping_tabs, pattern_path):
		# Key on ID. Lookup is responsibility of calling script.
		# check go is a brain OR owl-api ontology object
		## Wouldn't it be better to pass just the row(s) required?
		owl_map = mapping_tabs.RCV_id_2_owlMap(RCV_id)
		self.go = mapping_tabs.go
		"""Initialise map object: go = a Brain ontology object, 'RCV_ID' is the Roche term ID, manual_map is the mapping table as a list of dicts, keyed on column, owl_map is a row_column_dict of the owl mapping table."""
		self.manual_list = mapping_tabs.RCV_id_2_man_map(RCV_id) # Old manually curated mapping from Roche
		self.generated_list = [] # Results of running OWL queries 
		self.blacklist = []  # Terms blacklisted by Roche annotators
		self.id_name = {}  # hash lookup for names of GO terms in lists (should this really be bodged in here?!)
		"""go = go ontology object; RochCVterm = a single term from RocheCV; manual_map = colDict of manual map; owl_map = ColRowDict of owl mapping file"""
		self.RCV_id = RCV_id
		self.pattern_name = owl_map['Applied pattern']
		dc = { 'key_class': ( owl_map['Key Class Name'], owl_map['Key Class ID'] )}
		self.appl_pattern  = gen_applied_pattern_from_json(pattern_path + self.pattern_name + ".json", dc, self.go)
		self.class_expression = self.appl_pattern.equivalentTo
		for m in manual_map:
			self.manual_list.append(m['GO_ID'])
		self.update_map()
		self.update_id_name()

		
	def validate_owl_map(self):
		"""Runs a bunch of validation checks on OWL MAP:
		Does ontology know key class;
		Does key class name match ID..."""
		# STUB!
		return

		
	def update_map(self):
		"""Updates mapping generated from owl class expression"""
		## Map should be updated when object is initialised! 
		self.generated_list.extend(self.go.getSubClasses(self.class_expression, 0))  # This assumes an OWL object.  But should probably be querying via OWLtools using hermit in order to use OR.
		self.generated_list.extend(self.go.getEquivalentClasses(self.class_expression))
		# brain.getEquivalentClasses does not return named query class.  
		# This checks if the query class expression is a GO_ID and if yes, appends it to the generated list.
		if re.match("GO\_\d{7}$", self.class_expression):
			self.generated_list.append(self.class_expression)
		
	def gen_report(self, report_tab):
		"""Generate report for 'Roche CV term'.  Arg (report) = a results table as row_column_dict."""
		### Spec - this only needs to remember content if there is a 1 in either checked or blacklisted.
		### It should never make inferences about 
		keys = set(self.generated_list) | set(self.manual_list) # Make union of two lists => complete set of keys.
		for key in keys:
			# Add key for row, if not already present
			if key not in report_tab:
				report_tab[key] = { 'checked': 0, 'blacklisted': 0 }
			# Populate row
			report_tab[key]['name'] = self.id_name[key]
			report_tab[key]['ID'] = key
			if key in self.manual_list:
				report_tab[key]['manual'] = 1
				report_tab[key]['checked'] = 1
			else:
				report_tab[key]['manual'] = 0
			if key in self.generated_list:
				report_tab[key]['auto'] = 1
			else:
				report_tab[key]['auto'] = 0
			# 
			if report_tab[key]['blacklisted']:
				self.blacklist.append(key)  # Not using this right now...
			
			#  Need something 
			rtk = report_tab.keys()
			for k in rtk:
				if k not in keys:
					del report_tab[k]
					

	def update_id_name(self, ont):
		# Perhaps should be dealt with outside?  Could have a class object.  But then might be easier to do all this purely in OWL/Brain!
		idList = set(self.generated_list) | set(self.manual_list)
		for ID in idList:
			self.id_name[ID]=ont.getLabel(ID)

