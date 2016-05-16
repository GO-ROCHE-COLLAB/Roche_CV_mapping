### Quick Guide to files used in the  automated mapping of RCV to GO .

* [Original manual, RCV to GO  mapping](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/manual_map_with_ids.tsv)

* [RCV -> OWL Mapping table](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/owl_map.tsv).  Columns:
  * Entries in the column: 'Applied pattern' refer to the design patterns used for the mapping.  These are listed in the [patterns directory](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/tree/master/patterns).  Patterns are specified using [dead simple OWL design patterns]()  (Osumi-Sutherland et al., 2016 In Press).  The patterns used take only one variable - specified in the 
Object properties for queries live here:

* The novel object properties and object property axioms used for the mapping can be found in [GO_ROCHE_importer.owl](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/owl/GO_ROCHE_importer.owl).

* [Results summary](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/results_summary.md), including automated definitions, links to tickets and individual results tables.

* [Mapping stats](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/stats.tsv)

* [Combined manual and automated mapping](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/blob/master/mapping_tables/results/combined_results.tsv)
