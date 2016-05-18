### Quick Guide to files used in the  automated mapping of RCV to GO.

* [Original manual, RCV -> GO  mapping](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/manual_map_with_ids.tsv)

* [RCV -> OWL Mapping table](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/owl_map.tsv).  Columns:
  * Entries in the column: 'Applied pattern' refer to the design patterns used for the mapping.  These are listed in the [patterns directory](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/tree/master/patterns).  Patterns are specified using [dead simple OWL design patterns](https://github.com/dosumis/dead_simple_owl_design_patterns)  (Osumi-Sutherland et al., 2016 In Press).  The patterns used take only one variable - specified in the key\_class columns.  The main reason for using patterns is rolling human readable definitions.  Logical definitions follow a sufficiently simple pattern that they could have been specified by naming a relationship in to a key\_class in the mapping table.

* The novel object properties and object property axioms used for the mapping can be found in [GO_ROCHE_importer.owl](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/owl/GO_ROCHE_importer.owl).

* [Results summary](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/results_summary.md), including automated definitions, links to tickets and individual results tables.

* [Mapping stats](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/stats.tsv)

* [Combined manual and automated mapping](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/combined_results.tsv)
