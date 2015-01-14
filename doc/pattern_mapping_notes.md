# Description of mapping between RCV class types and 

Many RCV class names follow predictable patterns.  In many cases, the mapping pattern that resulted in the best match to the manual mapping tracked these naming patterns.  This document traces these mappings and notes their limitations compared to what was typically found in the manual mapping.  Each RCV name pattern -> mapping pattern is named using the convention:

RCV_name_pattern:key_class_type:design_pattern

## Cell:Cell:CL_anat_super_query

RCV term named for cell; mapped to class from CL; design pattern [CL_anat_super_query](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/patterns/CL_anat_super_query.md), which produces terms with the definition: "A process in which a CELL_X participates or that occur in CELL_X or which results in the developmental progression of a structure that will form CELL_X."

__Limitations:__ 

- misses regulation of these processes.

__Examples:__

__Exceptions:__

## CC:CC:cellular_component_and_related_processes

RCV term named for cellular component ; mapped to class from GO:celluar_component; design pattern [cellular_component_and_related_processes](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/patterns/cellular_component_and_related_processes.md), which produces terms with the definition: "A CCX or a process that results in organisation of a CCX or that has a CCX as a participant."

__Limitations:__ 

- misses regulation of related processes.

__Examples:__

[synapse](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/33)

__Exceptions:__

None

## metabolism:metabolic_process:equivalence

RCV term named for ; mapped to class from ; design pattern [](), which produces terms with the definition: ""

__Limitations:__ 

- Manual mappings include transport.  Automating these would require a pattern with disjunction.

__Examples:__

__Exceptions:__


## chemical:participant_chemical

RCV term named for ; mapped to class from ; design pattern [](), which produces terms with the definition: ""

__Limitations:__ 

- misses regulation of these processes.

__Examples:__

__Exceptions:__


## development:development:is_a_OR_part_of_OR_regulates

RCV term named for ; mapped to class from ; design pattern [](), which produces terms with the definition: ""

__Limitations:__ 

__Examples:__

__Exceptions:__

## anatomy:development:is_a_OR_part_of_OR_regulates

RCV term named for ; mapped to class from ; design pattern [](), which produces terms with the definition: ""

__Limitations:__ 

- misses regulation of these processes.

__Examples:__

__Exceptions:__

## signalling_pathway:signalling_pathway:is_a_OR_part_of_OR_regulates

RCV term named for ; mapped to class from ; design pattern [](), which produces terms with the definition: ""

__Limitations:__ 


## MF:MF:is_a_OR_part_of_OR_regulates_OR_capable_of

RCV term named for a molecular function (e.g. enzyme activity); mapped to class from GO:molecular_function; design pattern [is_a_OR_part_of_OR_regulates_OR_capable_of](), which produces terms with the definition: ""

__Limitations:__ 


__Examples:__

__Exceptions:__

__Examples:__

__Exceptions:__







