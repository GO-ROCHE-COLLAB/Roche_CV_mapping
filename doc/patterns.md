## Documentation of ontology design patterns used in mapping

### X metabolism terms

RCV X metabolism terms should encompass both metabolism and transport.
tRNA biosynthesis terms should be excluded.

Mapping pattern currently used: _equivalentTo_ GO:'X metabolic process'.  This misses transport terms.  
In order to include transport terms in automated mapping we would neeed to take 2 class expression and combine the results.  This would require additional functionality in the mapping system.

### chemicals

pattern: has\_participant some ChEBI:chemical_entity

### cell types

Processes that cells participate in.  Development terms are not included.  May also be useful to include processes that only occur in the specified cell type.

Pattern:  has\_participant some CL:cell  

Note - cell 

### development

## anatomy
