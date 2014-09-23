## A summary of the current results, including links to results files.

* Notch signaling pathway RCV_000027
  * Pattern: Equivalence
  * map summary: Roche_cvt: RCV_000027; class_expression GO_0007219; manual_list_count 10, generated_list_count 9
  * [Results](Notch_signaling_pathway_RCV_000027.tsv)

* G-protein RCV_000017
  * Notes: Manual mapping is only regulation of GPCR signaling pathway terms whose names explicilty reference  activity GPCR signaling
  * Results: N/A Job not run. Specification marked as preliminary or missing.

* wound healing RCV_000356
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000356; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0042060; manual_list_count 12, generated_list_count 91
  * [Results](wound_healing_RCV_000356.tsv)

* DNA silencing RCV_000012
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000012; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0016458; manual_list_count 44, generated_list_count 100
  * [Results](DNA_silencing_RCV_000012.tsv)

* B cells RCV_000001
  * Pattern: has_participant_cell
  * map summary: Roche_cvt: RCV_000001; class_expression RO_0000057 some CL_0000236; manual_list_count 124, generated_list_count 60
  * Notes: Getting some undesirable results because of overly broad axioms on 'B-cell mediated immune response'.  Missing results are becuase we need to include 'regulates some (has_participant some 'B cell') + has_participant some (develops_into some 'B cell'.  Requires 3 queries OR using HermiT.
  * [Results](B_cells_RCV_000001.tsv)

* NGF pathway RCV_000025
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000025; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0038180; manual_list_count 3, generated_list_count 2
  * Notes: Manual mapping includes 
  * [Results](NGF_pathway_RCV_000025.tsv)

* DNA binding process RCV_000005
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000005; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0003677; manual_list_count 38, generated_list_count 142
  * Notes: 'DNA binding process' + subclasses maybe sufficient.  Extra classes found over manual list look justified.
  * [Results](DNA_binding_process_RCV_000005.tsv)

* DNA repair RCV_000009
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000009; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006281; manual_list_count 49, generated_list_count 111
  * Notes: Manual map includes the odd regulation term and complex, so a query that brings in both of these may be justified.  But including these results in a much larger list than the manual one.
  * [Results](DNA_repair_RCV_000009.tsv)

* NK cells RCV_000026
  * Pattern: has_participant_cell
  * map summary: Roche_cvt: RCV_000026; class_expression RO_0000057 some CL_0000623; manual_list_count 62, generated_list_count 14
  * [Results](NK_cells_RCV_000026.tsv)

* SMAD pathway RCV_000033
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000033; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0060395; manual_list_count 4, generated_list_count 1
  * [Results](SMAD_pathway_RCV_000033.tsv)

* RNA interference RCV_000031
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000031; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0016246; manual_list_count 3, generated_list_count 9
  * Notes: Manual mapping seems to be to antisense RNA terms that are not necessarily connected with RNA interference?
  * [Results](RNA_interference_RCV_000031.tsv)

* GPCR signaling RCV_000019
  * Pattern: Equivalence
  * map summary: Roche_cvt: RCV_000019; class_expression GO_0007186; manual_list_count 7, generated_list_count 89
  * Notes: Manual mapping is only adenylate-cyclase signaling pathway. Should it be renamed, or would a broader mapping be appropriate ?
  * [Results](GPCR_signaling_RCV_000019.tsv)

* DNA recombination RCV_000008
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000008; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006310; manual_list_count 3, generated_list_count 146
  * Notes: Massively incomplete manual map?  Subclasses of recombination alone => 51 classes, but this has only 3 manual mappings!
  * [Results](DNA_recombination_RCV_000008.tsv)

* NF-kappaB pathway RCV_000024
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000024; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0007249; manual_list_count 2, generated_list_count 5
  * [Results](NF-kappaB_pathway_RCV_000024.tsv)

* SP1A pathway RCV_000034
  * Pattern: Equivalence
  * map summary: Roche_cvt: RCV_000034; class_expression GO_0003376; manual_list_count 1, generated_list_count 2
  * [Results](SP1A_pathway_RCV_000034.tsv)

* DNA replication negative RCV_000011
  * Pattern: Equivalence
  * map summary: Roche_cvt: RCV_000011; class_expression GO_0008156; manual_list_count 1, generated_list_count 15
  * Notes: Only 1 in this class! - not related to manually mapped class!
  * [Results](DNA_replication_negative_RCV_000011.tsv)

* MAPK signalling RCV_000022
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000022; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0000165; manual_list_count 37, generated_list_count 92
  * [Results](MAPK_signalling_RCV_000022.tsv)

* Malpighian tubule stellate cell RCV_000023
  * Pattern: results in developmental progression of
  * map summary: Roche_cvt: RCV_000023; class_expression RO_0002295 some CL_1000155; manual_list_count 1, generated_list_count 1
  * [Results](Malpighian_tubule_stellate_cell_RCV_000023.tsv)

* STATx phosphorylation RCV_000035
  * Pattern: Equivalence
  * map summary: Roche_cvt: RCV_000035; class_expression GO_0007260; manual_list_count 9, generated_list_count 7
  * [Results](STATx_phosphorylation_RCV_000035.tsv)

* GTPase activity RCV_000020
  * Pattern: is_a_OR_part_of_OR_regulates_OR_capable_of
  * map summary: Roche_cvt: RCV_000020; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0003924; manual_list_count 10, generated_list_count 53
  * Notes: Manual mapping includes obsolete terms for individual G-protein subunits, automated mapping will pull in whole complex.
  * [Results](GTPase_activity_RCV_000020.tsv)

* CTGF RCV_000004
  * Notes: No axioms on key class.  Look into adding from Pro?
  * Results: N/A Job not run. Specification marked as preliminary or missing.

* zinc ion homeostasis RCV_000359
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000359; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0055069; manual_list_count 5, generated_list_count 6
  * Notes: GO axiomatisation insufficient?
  * [Results](zinc_ion_homeostasis_RCV_000359.tsv)

* FGF pathway RCV_000016
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000016; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0008543; manual_list_count 20, generated_list_count 30
  * [Results](FGF_pathway_RCV_000016.tsv)

* RNA splicing RCV_000032
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000032; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0008380; manual_list_count 47, generated_list_count 51
  * [Results](RNA_splicing_RCV_000032.tsv)

* DNA synthesis RCV_000013
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000013; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0071897; manual_list_count 3, generated_list_count 30
  * [Results](DNA_synthesis_RCV_000013.tsv)

* triglyceride RCV_000336
  * Pattern: has_participant_chemical
  * map summary: Roche_cvt: RCV_000336; class_expression RO_0000057 some CHEBI_17855; manual_list_count 9, generated_list_count 9
  * [Results](triglyceride_RCV_000336.tsv)

* PPAR pathway RCV_000030
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000030; class_expression GO_0035357; manual_list_count 4, generated_list_count 0
  * [Results](PPAR_pathway_RCV_000030.tsv)

* BMP pathway RCV_000003
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000003; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0030509; manual_list_count 33, generated_list_count 33
  * Notes: Missing binding, secretion ligand etc.  Need a way to ask for processes with BMP as participant.
  * [Results](BMP_pathway_RCV_000003.tsv)

* MAPK inactivation RCV_000021
  * Pattern: Equivalence
  * map summary: Roche_cvt: RCV_000021; class_expression GO_0043407; manual_list_count 17, generated_list_count 6
  * [Results](MAPK_inactivation_RCV_000021.tsv)

* T cells RCV_000037
  * Pattern: has_participant_cell
  * map summary: Roche_cvt: RCV_000037; class_expression RO_0000057 some CL_0000084; manual_list_count 247, generated_list_count 106
  * Notes: Also need inference of regulation of processes in which T cells participate?
  * [Results](T_cells_RCV_000037.tsv)

* BDNF pathway RCV_000002
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000002; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0031547; manual_list_count 7, generated_list_count 8
  * [Results](BDNF_pathway_RCV_000002.tsv)

* EGFR pathway RCV_000014
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000014; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0007173; manual_list_count 9, generated_list_count 24
  * [Results](EGFR_pathway_RCV_000014.tsv)

* DNA damage RCV_000006
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000006; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0042769; manual_list_count 41, generated_list_count 9
  * [Results](DNA_damage_RCV_000006.tsv)

* DNA replication RCV_000010
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000010; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006260; manual_list_count 42, generated_list_count 150
  * [Results](DNA_replication_RCV_000010.tsv)

* TCA metabolism RCV_000039
  * Pattern: has_participant_chemical
  * map summary: Roche_cvt: RCV_000039; class_expression RO_0000057 some CHEBI_35753; manual_list_count 7, generated_list_count 37
  * [Results](TCA_metabolism_RCV_000039.tsv)

* PNS development RCV_000029
  * Pattern: is_a_OR_part_of
  * map summary: Roche_cvt: RCV_000029; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0007422; manual_list_count 5, generated_list_count 30
  * [Results](PNS_development_RCV_000029.tsv)

* ERBB signaling pathway RCV_000015
  * Pattern: is_a_OR_part_of_OR_regulates
  * map summary: Roche_cvt: RCV_000015; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0038127; manual_list_count 1, generated_list_count 35
  * [Results](ERBB_signaling_pathway_RCV_000015.tsv)

