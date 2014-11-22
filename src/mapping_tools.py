#!/usr/bin/env jython -J-Xmx8000m
from uk.ac.ebi.brain.core import Brain
from owltools.graph import OWLGraphWrapper
import re
from pattern import gen_applied_pattern_from_json
import warnings
from tsv2pdm import tab


# Critique: why so much passing of data structures, rather than objects?
# Which bits could most easily and cleanly done with a DB?
## Clearly the RCV, manual mapping and owl_map files should live in a DB.
## A simple pattern table could also be useful for constraint purposes.



def load_ont(url):
	ont = Brain()
	ont.learn(url)
	return ont


class mappingTabs():
	"""A container for ontology and tables used in mapping + methods on these tables and sync between them."""
	# In lieu of a DB - which is clearly how this should be done!
	def __init__(self, manual_map, owl_map, RCV, go):
		"""manual_map is a list of dicts containing the manual mapping table;
		 owl_map is a dict(row) of dicts(columns) containing the OWL mapping table,
		 RCV is the Roche term table as a dict of dicts
		 go is a Brain object containing the ontology used for mapping."""
		self.manual_map = manual_map
		self.owl_map = owl_map
		self.go = go
		self.rcv = RCV
		self.obs_status = {} # A dictionary of manually mapped GO terms, with value = is obsolete True/False 
		self.update_manual_map_obs_stat()
		self.combined_results = tab()
		self.combined_results.headers = ["RCV_ID", "RCV_NAME", "GO_ID", "GO_NAME"]
	
	def RCV_id_2_owlMap(self, RCV_id):
		return self.owl_map[RCV_id]
		
	def RCV_id_2_man_map(self, RCV_id):
		out = []
		for i in self.manual_map:
			if i['RCV_ID'] == RCV_id:
				out.append(i)
		return out
	
	def update_manual_map_obs_stat(self):
		"""Does what is says on the tin"""
		gonto = self.go.getOntology()
		gogw = OWLGraphWrapper(gonto)
		for c in self.manual_map:
			obo_id = re.sub('_', ':', c['GO_ID']) # Hard to believe this is necessary!
			clazo = gogw.getOWLClassByIdentifier(obo_id)
			if gogw.isObsolete(clazo):
				warnings.warn("Obsolete class: %s"  %  c['GO_ID'])
				c['STATUS'] = 0
				self.obs_status[c['GO_ID']] = True
			else:
				self.obs_status[c['GO_ID']] = False

class map_obj:
	# Should this work on ids or names?  Seems wasteful to store both.
	def __str__(self):
		return "Roche_cvt: %s; class_expression %s; manual_list_count %d, generated_list_count %d" % (self.RCV_id, self.class_expression, len(self.manual_list), len(self.generated_list))
	def __init__ (self, RCV_id, mapping_tabs, pattern_path):
		"""Initialise map object: 
		'RCV_ID' is the Roche term ID,
		'mapping_tabs' = a mapping tab object
		pattern_path = path to pattern specification json files
		"""
		
		# Key on ID. Lookup is responsibility of calling script.
		self.rcv = mapping_tabs.rcv
		self.combined_results = mapping_tabs.combined_results.tab
		owl_map = mapping_tabs.RCV_id_2_owlMap(RCV_id)
		self.go = mapping_tabs.go
		self.obs_status = mapping_tabs.obs_status
		self.manual_list = []# Old manually curated mapping from Roche
		self.generated_list = [] # Results of running OWL queries 
		self.id_name = {}  # hash lookup for names of GO terms in lists (should this really be bodged in here?!)
		"""go = go ontology object; RochCVterm = a single term from RocheCV; manual_map = colDict of manual map; owl_map = ColRowDict of owl mapping file"""
		self.RCV_id = RCV_id
		self.pattern_name = owl_map['Applied pattern']
		self.status = owl_map['issue_state']
		dc = { 'key_class': ( owl_map['Key Class Name'], owl_map['Key Class ID'] )}
		self.appl_pattern  = gen_applied_pattern_from_json(pattern_path + self.pattern_name + ".json", dc, self.go)
		self.class_expression = self.appl_pattern.equivalentTo
		manual_map = mapping_tabs.RCV_id_2_man_map(RCV_id)
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
		"""Generate report for 'Roche CV term'.  Arg (report_tab) = a results table as row_column_dict."""
		### Spec - needs to remember content if there is a 1 in either checked or blacklisted.
		### DONE Overloading blacklist: blacklist obsolete terms.  (Really would be better to have extra column!)
		
		keys = set(self.generated_list) | set(self.manual_list) # Make union of two lists => complete set of keys.
		for key in keys:
			# Add key for row, if not already present
			if key not in report_tab:
				report_tab[key] = { 'checked': 0, 'blacklisted': 0, 'is_obsolete': 0 } # Initialize 
			# Populate row
			report_tab[key]['name'] = self.id_name[key]
			report_tab[key]['ID'] = key
			if key in self.manual_list:
				report_tab[key]['manual'] = 1
				report_tab[key]['checked'] = 1
				# black list obsolete GO terms in manual mapping.
				if self.obs_status[key]:
					report_tab[key]['blacklisted'] = 1
					report_tab[key]['is_obsolete'] = 1
			else:
				report_tab[key]['manual'] = 0
			if key in self.generated_list:
				report_tab[key]['auto'] = 1
			else:
				report_tab[key]['auto'] = 0
			# Make sure edited content not turned to strings. # Should really wrap in try
			report_tab[key]['checked'] = int(report_tab[key]['checked'] )
			report_tab[key]['blacklisted'] = int(report_tab[key]['blacklisted'] )
			report_tab[key]['is_obsolete'] = int(report_tab[key]['is_obsolete'] )

			
			# Delete mapping from report if no longer in manual or auto.
		rtk = report_tab.keys()
		for k in rtk:
			if k not in keys:
				del report_tab[k]
				
		# Makes sure all columns that should be 0/1 are:


		# Update combined mapping
		if self.status == 'closed - mapping completed':
			self._append_to_combined_mapping(report_tab)
			
	def _append_to_combined_mapping(self, report_tab):
		"""report_tab = results table as dict of dicts, keyed on RCV_id"""
		# Spec:  Append to compound table - combined manual & auto mappings that are not blacklisted
		for d in report_tab.values():
			rd = {}
			if d['checked'] and not d['blacklisted']:
				rd['RCV_NAME'] = self.rcv[self.RCV_id]['RCV_NAME']
				rd['RCV_ID'] = self.RCV_id
				rd['GO_ID'] = d['ID']
				rd['GO_NAME'] = d['name']
			# only append to combined results if populated.	
			if rd:
				self.combined_results.append(rd)
	
			

	def update_id_name(self):
		# Perhaps should be dealt with outside?  Could have a class object.  But then might be easier to do all this purely in OWL/Brain!
		idList = set(self.generated_list) | set(self.manual_list)
		for ID in idList:
			self.id_name[ID]=self.go.getLabel(ID)

