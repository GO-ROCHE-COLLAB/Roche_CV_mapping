## A summary of the current results, including links to results files.

* B cells ; RCV_000001:
  * Query: has_participant some 'B cell' 
  * map summary: Roche_cvt: RCV_000001; class_expression RO_0000057 some CL_0000236; manual_list_count 124, generated_list_count 60.
  * Notes: Getting some undesirable results because of overly broad axioms on 'B-cell mediated immune response'.  Missing results are becuase we need to include 'regulates some (has_participant some 'B cell') + has_participant some (develops_into some 'B cell'.  Requires 3 queries OR using HermiT.
  * [Results](B_cells_RCV_000001.tsv)
* DNA recombination ; RCV_000008:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000008; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006310; manual_list_count 3, generated_list_count 146.
  * Notes: Massively incomplete manual map?  Subclasses of recombination alone => 51 classes, but this has only 3 manual mappings!
  * [Results](DNA_recombination_RCV_000008.tsv)
* DNA binding process ; RCV_000005:
  * Query: improper_part_of some 'DNA binding' 
  * map summary: Roche_cvt: RCV_000005; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0003677; manual_list_count 38, generated_list_count 139.
  * Notes: 'DNA binding process' + subclasses maybe sufficient.  Extra classes found over manual list look justified.
  * [Results](DNA_binding_process_RCV_000005.tsv)
* DNA repair ; RCV_000009:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000009; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006281; manual_list_count 49, generated_list_count 111.
  * Notes: Manual map includes the odd regulation term and complex, so a query that brings in both of these may be justified.  But including these results in a much larger list than the manual one.
  * [Results](DNA_repair_RCV_000009.tsv)
* wound healing ; RCV_000356:
  * Query: regulates_or_part_of some 'wounding healing' 
  * map summary: Roche_cvt: RCV_000356; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0042060; manual_list_count 12, generated_list_count 91.
  * Notes: 
  * [Results](wound_healing_RCV_000356.tsv)
* DNA silencing ; RCV_000012:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000012; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0016458; manual_list_count 44, generated_list_count 100.
  * Notes: 
  * [Results](DNA_silencing_RCV_000012.tsv)
* DNA damage ; RCV_000006:
  * Query: improper_part_of some 'DNA damage response' 
  * map summary: Roche_cvt: RCV_000006; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0042769; manual_list_count 41, generated_list_count 9.
  * Notes: 
  * [Results](DNA_damage_RCV_000006.tsv)
* BMP pathway ; RCV_000003:
  * Query: part_of_or_regulates some 'BMP signalling pathway' 
  * map summary: Roche_cvt: RCV_000003; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0030509; manual_list_count 33, generated_list_count 33.
  * Notes: Missing binding, secretion ligand etc.  Need a way to ask for processes with BMP as participant.
  * [Results](BMP_pathway_RCV_000003.tsv)
* DNA replication ; RCV_000010:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000010; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006260; manual_list_count 42, generated_list_count 150.
  * Notes: 
  * [Results](DNA_replication_RCV_000010.tsv)
* zzinc ion homeostasis ; RCV_000359:
  * Query: improper_part_of some 'zinc ion homeostasis' 
  * map summary: Roche_cvt: RCV_000359; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0055069; manual_list_count 5, generated_list_count 6.
  * Notes: GO axiomatisation insufficient?
  * [Results](zinc_ion_homeostasis_RCV_000359.tsv)
* FGF pathway ; RCV_000016:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000016; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0008543; manual_list_count 20, generated_list_count 30.
  * Notes: 
  * [Results](FGF_pathway_RCV_000016.tsv)
* DNA synthesis ; RCV_000013:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000013; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0071897; manual_list_count 3, generated_list_count 30.
  * Notes: 
  * [Results](DNA_synthesis_RCV_000013.tsv)
* BDNF pathway ; RCV_000002:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000002; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0031547; manual_list_count 7, generated_list_count 8.
  * Notes: 
  * [Results](BDNF_pathway_RCV_000002.tsv)
* triglyceride ; RCV_000336:
  * Query: has_participant some triglyceride 
  * map summary: Roche_cvt: RCV_000336; class_expression RO_0000057 some CHEBI_17855; manual_list_count 9, generated_list_count 9.
  * Notes: 
  * [Results](triglyceride_RCV_000336.tsv)
* EGFR pathway ; RCV_000014:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000014; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0007173; manual_list_count 9, generated_list_count 24.
  * Notes: 
  * [Results](EGFR_pathway_RCV_000014.tsv)
* ERBB signaling pathway ; RCV_000015:
  * Query: part_of_or_regulates 
  * map summary: Roche_cvt: RCV_000015; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0038127; manual_list_count 1, generated_list_count 35.
  * Notes: 
  * [Results](ERBB_signaling_pathway_RCV_000015.tsv)
