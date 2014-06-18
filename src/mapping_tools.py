#!/usr/bin/env jython -J-Xmx8000m
from tsv2pdm import tsv2rowDict
from uk.ac.ebi.brain.core import Brain

def load_ont(url):
	ont = Brain()
	ont.learn(url)
	return ont

def brain2graphWrapper(ont):
	onto = ont.getOntology()
    return OWLGraphWrapper(onto)

def roll_basic_pattern (key_class):
    return "(has_participant some) %s or (regulates some (has_particpant some %s))" % (key_class, key_class) # If using this pattern, will need OWLtools/HermiT.

class map_obj(go, RocheCVterm, manual_map, owl_map):
	"""go = go ontology object; RochCVterm = a single term from RocheCV; manual_map = colDict of manual map; owl_map = ColRowDict of owl mapping file"""
	# check ont is a brain OR owl-api ontology object
    class_expression = owl_map['OWL class expression (IDs)'][RocheCVterm] # Class expression used to generate list
    manual_list = [] # Old manually curated mapping from Roche
	for m in manual_map:
		if m['Roche CV'] == RocheCVterm:
			manual_list.append(m['GO term ID'])
    generated_list = [] # Results of running OWL queries 
    blacklist = []  # Not yet supported.
	report = []
	name_id = gen_name_id_dict(go)  # Very inefficient !!!
	def update_map(self):
		"""Updates mapping generated from owl class expression"""
		## Map should be updated when object is initialised! 
		self.generated_list = self.ont.getSubClasses(self.class_expression, 0)  # This assumes an OWL object.  But should probably be querying via OWLtools using hermit in order to use OR.
    def gen_report(self):
		"""Report format: Col1 manual map term name, Col2 manual map term ID, Col3 Generated mapping (names), Col4 Generated mapping (IDs), Col5 checked, Col6 blacklist.
		Ordering: Alphanumeric sort col1, Col2 cell occupied if matching Col1.  Then Alphanumeric sort remaning term in Col2"""
		
	def print_report(self):
		print = "%s\t%s\t%s\t%s\t%s\t%s\n" % ('manual map name', 'manual map id', 'auto map name', 'auto map id', 'checked', 'blaclisted')
		print self.report
		
def gen_name_id_dict(ont):
	name_id = {}
	classList = ont.SubClasses("Thing", 0)
	for claz in classList:
		name_id[claz] = ont.getLabel[claz]
	return name_id
	

#map_file = open("../mapping_tables/...", "r")

#map_tab = tsv2rowDict(map)

#map_obj
