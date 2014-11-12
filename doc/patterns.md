# Documentation of ontology design patterns used in mapping

## X metabolism terms

RCV X metabolism terms should encompass both metabolism and transport.
tRNA biosynthesis terms should be excluded.

Mapping pattern currently used: _equivalentTo_ GO:'X metabolic process'.  This misses transport terms.  
In order to include transport terms in automated mapping we would neeed to take 2 class expression and combine the results.  This would require additional functionality in the mapping system.

## chemicals

has_participant some ChEBI:chemical_entity

## cell types

has_participant some CL:cell  

## development


## anatomy
