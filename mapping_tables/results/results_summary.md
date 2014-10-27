## A summary of the current results, including links to results files & issues.

#### B cells RCV_000001
* Key class: [B cell](http://www.ebi.ac.uk/ontology-lookup/?termId=CL:0000236)
* Pattern: [has_participant_cell](../../patterns/has_participant_cell.md)
* Definition: A process in which a B cell participates.
* map summary: Roche_cvt: RCV_000001; class_expression RO_0000057 some CL_0000236; manual_list_count 124, generated_list_count 60
* Notes: Internal: Getting some undesirable results because of overly broad axioms on 'B-cell mediated immune response'.  Missing results are becuase we need to include 'regulates some (has_participant some 'B cell') + has_participant some (develops_into some 'B cell'.  Requires 3 queries OR using HermiT.
* [Results](B_cells_RCV_000001.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/44)
* Status: closed

#### TLRx pathway RCV_000041
* Key class: [toll-like receptor signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0002224)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: toll-like receptor signaling pathway OR a part of toll-like receptor signaling pathway OR a process that regulates toll-like receptor signaling pathway
* map summary: Roche_cvt: RCV_000041; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0002224; manual_list_count 87, generated_list_count 85
* [Results](TLRx_pathway_RCV_000041.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/64)
* Status: open

#### DNA repair RCV_000009
* Key class: [DNA repair](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0006281)
* Pattern: [is_a_OR_part_of_OR_regulates_OR_capable_of](../../patterns/is_a_OR_part_of_OR_regulates_OR_capable_of.md)
* Definition: DNA repair OR a part of DNA repair OR a process that regulates DNA repair OR a cell component that functions in DNA repair.
* map summary: Roche_cvt: RCV_000009; class_expression 386a1f76_b26e_477f_8e50_6e4dab26bc3b some GO_0006281; manual_list_count 142, generated_list_count 137
* Notes: Laura: The manual map includes the odd regulation term and complex, so I've used a pattern that includes both of these.  But including these results in a much larger list than the manual one.  Should we keep this pattern?
* [Results](DNA_repair_RCV_000009.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/13)
* Status: closed

#### TGF beta pathway RCV_000040
* Key class: [cellular response to transforming growth factor beta stimulus](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0071560)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: cellular response to transforming growth factor beta stimulus OR a part of cellular response to transforming growth factor beta stimulus OR a process that regulates cellular response to transforming growth factor beta stimulus
* map summary: Roche_cvt: RCV_000040; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0071560; manual_list_count 42, generated_list_count 20
* Notes: 1
* [Results](TGF_beta_pathway_RCV_000040.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/68)
* Status: open

#### NF-kappaB pathway RCV_000024
* Key class: [I-kappaB kinase/NF-kappaB signaling](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0007249)
* Pattern: [is_a_OR_part_of](../../patterns/is_a_OR_part_of.md)
* Definition: I-kappaB kinase/NF-kappaB signaling OR a part of (some) I-kappaB kinase/NF-kappaB signaling.
* map summary: Roche_cvt: RCV_000024; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0007249; manual_list_count 2, generated_list_count 5
* [Results](NF-kappaB_pathway_RCV_000024.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/16)
* Status: closed

#### SP1A pathway RCV_000034
* Key class: [sphingosine-1-phosphate signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0003376)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for sphingosine-1-phosphate signaling pathway.
* map summary: Roche_cvt: RCV_000034; class_expression GO_0003376; manual_list_count 1, generated_list_count 3
* [Results](SP1A_pathway_RCV_000034.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/22)
* Status: closed

#### Notch signaling pathway RCV_000027
* Key class: [Notch signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0007219)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for Notch signaling pathway.
* map summary: Roche_cvt: RCV_000027; class_expression GO_0007219; manual_list_count 10, generated_list_count 10
* [Results](Notch_signaling_pathway_RCV_000027.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/48)
* Status: open

#### DNA replication negative RCV_000011
* Key class: [negative regulation of DNA replication](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0008156)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for negative regulation of DNA replication.
* map summary: Roche_cvt: RCV_000011; class_expression GO_0008156; manual_list_count 1, generated_list_count 20
* Notes: Laura: Only 1 automated mapping. Not related to manually mapped class! Can you suggest a different definition/key class mapping?
* [Results](DNA_replication_negative_RCV_000011.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/20)
* Status: open

#### G-protein RCV_000017
* Notes: Laura: Having trouble automating this as its meaning seems much more constrained than implied my the name.  Manual mapping is only regulation of GPCR signaling pathway terms whose names explicilty reference  activity GPCR signaling. Is a broad interpretation correct, or should change the name to positive 
* Results: N/A Job not run. Specification marked as preliminary or missing.

#### DNA silencing RCV_000012
* Key class: [chromatin silencing](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0006342)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: chromatin silencing OR a part of chromatin silencing OR a process that regulates chromatin silencing
* map summary: Roche_cvt: RCV_000012; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006342; manual_list_count 44, generated_list_count 46
* [Results](DNA_silencing_RCV_000012.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/61)
* Status: open

#### DNA binding process RCV_000005
* Key class: [DNA binding process](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0003677)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for DNA binding process.
* map summary: Roche_cvt: RCV_000005; class_expression GO_0003677; manual_list_count 38, generated_list_count 142
* Notes: Laura: Looks good?
* [Results](DNA_binding_process_RCV_000005.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/40)
* Status: closed

#### TRAIL production RCV_000043
* Key class: [TRAIL biosynthetic process](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0045553)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for TRAIL biosynthetic process.
* map summary: Roche_cvt: RCV_000043; class_expression GO_0045553; manual_list_count 5, generated_list_count 1
* [Results](TRAIL_production_RCV_000043.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/67)
* Status: open

#### SMAD pathway RCV_000033
* Key class: [SMAD protein signal transduction](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0060395)
* Pattern: [is_a_OR_part_of](../../patterns/is_a_OR_part_of.md)
* Definition: SMAD protein signal transduction OR a part of (some) SMAD protein signal transduction.
* map summary: Roche_cvt: RCV_000033; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0060395; manual_list_count 4, generated_list_count 1
* [Results](SMAD_pathway_RCV_000033.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/46)
* Status: open

#### GPCR signaling RCV_000019
* Key class: [G-protein coupled receptor signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0007186)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for G-protein coupled receptor signaling pathway.
* map summary: Roche_cvt: RCV_000019; class_expression GO_0007186; manual_list_count 40, generated_list_count 91
* Notes: Manual mapping is only adenylate-cyclase signaling pathway. Should it be renamed, or would a broader mapping be appropriate ?
* [Results](GPCR_signaling_RCV_000019.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/14)
* Status: open

#### DNA recombination RCV_000008
* Key class: [DNA recombination](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0006310)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for DNA recombination.
* map summary: Roche_cvt: RCV_000008; class_expression GO_0006310; manual_list_count 3, generated_list_count 52
* Notes: Laura: Perhaps this is just very incomplete? There are only 3 manual mappings.  The key class looks justified, but has 51 classes.  If you need a more constrained definition, can you suggest one?
* [Results](DNA_recombination_RCV_000008.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/37)
* Status: open

#### wound healing RCV_000356
* Key class: [wound healing](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0042060)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: wound healing OR a part of wound healing OR a process that regulates wound healing
* map summary: Roche_cvt: RCV_000356; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0042060; manual_list_count 12, generated_list_count 91
* [Results](wound_healing_RCV_000356.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/23)
* Status: open

#### NGF pathway RCV_000025
* Key class: [neurotrophin signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0038180)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: neurotrophin signaling pathway OR a part of neurotrophin signaling pathway OR a process that regulates neurotrophin signaling pathway
* map summary: Roche_cvt: RCV_000025; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0038180; manual_list_count 3, generated_list_count 5
* [Results](NGF_pathway_RCV_000025.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/65)
* Status: open

#### NK cells RCV_000026
* Key class: [natural killer cell](http://www.ebi.ac.uk/ontology-lookup/?termId=CL:0000623)
* Pattern: [has_participant_cell](../../patterns/has_participant_cell.md)
* Definition: A process in which a natural killer cell participates.
* map summary: Roche_cvt: RCV_000026; class_expression RO_0000057 some CL_0000623; manual_list_count 62, generated_list_count 14
* [Results](NK_cells_RCV_000026.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/47)
* Status: open

#### RNA interference RCV_000031
* Key class: [RNA interference](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0016246)
* Pattern: [is_a_OR_part_of](../../patterns/is_a_OR_part_of.md)
* Definition: RNA interference OR a part of (some) RNA interference.
* map summary: Roche_cvt: RCV_000031; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0016246; manual_list_count 3, generated_list_count 12
* Notes: Manual mapping seems to be to antisense RNA terms that are not necessarily connected with RNA interference?
* [Results](RNA_interference_RCV_000031.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/53)
* Status: open

#### UDP metabolism RCV_000044
* Key class: [UDP-sugar](http://www.ebi.ac.uk/ontology-lookup/?termId=CHEBI:17297)
* Pattern: [has_participant_chemical](../../patterns/has_participant_chemical.md)
* Definition: A process in which some UDP-sugar participates.
* map summary: Roche_cvt: RCV_000044; class_expression RO_0000057 some CHEBI_17297; manual_list_count 38, generated_list_count 38
* [Results](UDP_metabolism_RCV_000044.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/69)
* Status: open

#### MAPK signalling RCV_000022
* Key class: [MAPK cascade](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0000165)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: MAPK cascade OR a part of MAPK cascade OR a process that regulates MAPK cascade
* map summary: Roche_cvt: RCV_000022; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0000165; manual_list_count 37, generated_list_count 92
* [Results](MAPK_signalling_RCV_000022.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/35)
* Status: open

#### STATx phosphorylation RCV_000035
* Key class: [tyrosine phosphorylation of stat protein](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0007260)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for tyrosine phosphorylation of stat protein.
* map summary: Roche_cvt: RCV_000035; class_expression GO_0007260; manual_list_count 9, generated_list_count 8
* [Results](STATx_phosphorylation_RCV_000035.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/50)
* Status: closed

#### FGF pathway RCV_000016
* Key class: [fibroblast growth factor receptor signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0008543)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: fibroblast growth factor receptor signaling pathway OR a part of fibroblast growth factor receptor signaling pathway OR a process that regulates fibroblast growth factor receptor signaling pathway
* map summary: Roche_cvt: RCV_000016; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0008543; manual_list_count 20, generated_list_count 30
* [Results](FGF_pathway_RCV_000016.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/57)
* Status: open

#### RNA splicing RCV_000032
* Key class: [RNA splicing](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0008380)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: RNA splicing OR a part of RNA splicing OR a process that regulates RNA splicing
* map summary: Roche_cvt: RCV_000032; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0008380; manual_list_count 47, generated_list_count 51
* [Results](RNA_splicing_RCV_000032.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/52)
* Status: closed

#### DNA synthesis RCV_000013
* Key class: [DNA biosynthetic process](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0071897)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: DNA biosynthetic process OR a part of DNA biosynthetic process OR a process that regulates DNA biosynthetic process
* map summary: Roche_cvt: RCV_000013; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0071897; manual_list_count 3, generated_list_count 30
* [Results](DNA_synthesis_RCV_000013.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/60)
* Status: closed

#### BMP pathway RCV_000003
* Key class: [BMP pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0030509)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: BMP pathway OR a part of BMP pathway OR a process that regulates BMP pathway
* map summary: Roche_cvt: RCV_000003; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0030509; manual_list_count 33, generated_list_count 33
* Notes: Internal: Missing binding, secretion ligand etc.  Need a way to ask for processes with BMP as participant.
* [Results](BMP_pathway_RCV_000003.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/42)
* Status: open

#### MAPK inactivation RCV_000021
* Key class: [negative regulation of MAP kinase activity](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0043407)
* Pattern: [Equivalence](../../patterns/Equivalence.md)
* Definition: As for negative regulation of MAP kinase activity.
* map summary: Roche_cvt: RCV_000021; class_expression GO_0043407; manual_list_count 17, generated_list_count 7
* [Results](MAPK_inactivation_RCV_000021.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/34)
* Status: open

#### T cells RCV_000037
* Key class: [T cell](http://www.ebi.ac.uk/ontology-lookup/?termId=CL:0000084)
* Pattern: [has_participant_cell](../../patterns/has_participant_cell.md)
* Definition: A process in which a T cell participates.
* map summary: Roche_cvt: RCV_000037; class_expression RO_0000057 some CL_0000084; manual_list_count 247, generated_list_count 106
* Notes: Also need inference of regulation of processes in which T cells participate?
* [Results](T_cells_RCV_000037.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/49)
* Status: open

#### BDNF pathway RCV_000002
* Key class: [brain-derived neurotrophic factor receptor signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0031547)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: brain-derived neurotrophic factor receptor signaling pathway OR a part of brain-derived neurotrophic factor receptor signaling pathway OR a process that regulates brain-derived neurotrophic factor receptor signaling pathway
* map summary: Roche_cvt: RCV_000002; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0031547; manual_list_count 7, generated_list_count 8
* [Results](BDNF_pathway_RCV_000002.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/41)
* Status: closed

#### TCA metabolism RCV_000039
* Key class: [tricarboxylic acid anion](http://www.ebi.ac.uk/ontology-lookup/?termId=CHEBI:35753)
* Pattern: [has_participant_chemical](../../patterns/has_participant_chemical.md)
* Definition: A process in which some tricarboxylic acid anion participates.
* map summary: Roche_cvt: RCV_000039; class_expression RO_0000057 some CHEBI_35753; manual_list_count 7, generated_list_count 37
* [Results](TCA_metabolism_RCV_000039.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/62)
* Status: open

#### PNS development RCV_000029
* Key class: [peripheral nervous system development](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0007422)
* Pattern: [is_a_OR_part_of](../../patterns/is_a_OR_part_of.md)
* Definition: peripheral nervous system development OR a part of (some) peripheral nervous system development.
* map summary: Roche_cvt: RCV_000029; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0007422; manual_list_count 5, generated_list_count 27
* [Results](PNS_development_RCV_000029.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/39)
* Status: closed

#### TNF pathway RCV_000042
* Key class: [tumor necrosis factor-mediated signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0033209)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: tumor necrosis factor-mediated signaling pathway OR a part of tumor necrosis factor-mediated signaling pathway OR a process that regulates tumor necrosis factor-mediated signaling pathway
* map summary: Roche_cvt: RCV_000042; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0033209; manual_list_count 5, generated_list_count 8
* [Results](TNF_pathway_RCV_000042.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/66)
* Status: open

#### ERBB signaling pathway RCV_000015
* Key class: [ERBB signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0038127)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: ERBB signaling pathway OR a part of ERBB signaling pathway OR a process that regulates ERBB signaling pathway
* map summary: Roche_cvt: RCV_000015; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0038127; manual_list_count 1, generated_list_count 35
* [Results](ERBB_signaling_pathway_RCV_000015.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/55)
* Status: closed

#### GTPase activity RCV_000020
* Key class: [GTPase activity](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0003924)
* Pattern: [is_a_OR_part_of_OR_regulates_OR_capable_of](../../patterns/is_a_OR_part_of_OR_regulates_OR_capable_of.md)
* Definition: GTPase activity OR a part of GTPase activity OR a process that regulates GTPase activity OR a cell component that functions in GTPase activity.
* map summary: Roche_cvt: RCV_000020; class_expression 386a1f76_b26e_477f_8e50_6e4dab26bc3b some GO_0003924; manual_list_count 10, generated_list_count 54
* Notes: Manual mapping includes obsolete terms for individual G-protein subunits, automated mapping will pull in whole complex.
* [Results](GTPase_activity_RCV_000020.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/33)
* Status: open

#### CTGF RCV_000004
* Notes: Internal: No axioms on key class.  Look into adding from Pro?
* Results: N/A Job not run. Specification marked as preliminary or missing.

#### zinc ion homeostasis RCV_000359
* Key class: [zinc ion homeostasis](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0055069)
* Pattern: [is_a_OR_part_of](../../patterns/is_a_OR_part_of.md)
* Definition: zinc ion homeostasis OR a part of (some) zinc ion homeostasis.
* map summary: Roche_cvt: RCV_000359; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0055069; manual_list_count 7, generated_list_count 3
* Notes: Internal: GO axiomatisation insufficient?
* [Results](zinc_ion_homeostasis_RCV_000359.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/45)
* Status: open

#### triglyceride RCV_000336
* Key class: [triglyceride](http://www.ebi.ac.uk/ontology-lookup/?termId=CHEBI:17855)
* Pattern: [has_participant_chemical](../../patterns/has_participant_chemical.md)
* Definition: A process in which some triglyceride participates.
* map summary: Roche_cvt: RCV_000336; class_expression RO_0000057 some CHEBI_17855; manual_list_count 9, generated_list_count 9
* [Results](triglyceride_RCV_000336.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/43)
* Status: open

#### PPAR pathway RCV_000030
* Key class: [peroxisome proliferator activated receptor signaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0035357)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: peroxisome proliferator activated receptor signaling pathway OR a part of peroxisome proliferator activated receptor signaling pathway OR a process that regulates peroxisome proliferator activated receptor signaling pathway
* map summary: Roche_cvt: RCV_000030; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0035357; manual_list_count 4, generated_list_count 4
* [Results](PPAR_pathway_RCV_000030.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/54)
* Status: closed

#### EGFR pathway RCV_000014
* Key class: [epidermal growth factor receptor singaling pathway](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0007173)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: epidermal growth factor receptor singaling pathway OR a part of epidermal growth factor receptor singaling pathway OR a process that regulates epidermal growth factor receptor singaling pathway
* map summary: Roche_cvt: RCV_000014; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0007173; manual_list_count 9, generated_list_count 24
* [Results](EGFR_pathway_RCV_000014.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/56)
* Status: closed

#### DNA damage RCV_000006
* Key class: [DNA damage response, detection of DNA damage](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0042769)
* Pattern: [is_a_OR_part_of](../../patterns/is_a_OR_part_of.md)
* Definition: DNA damage response, detection of DNA damage OR a part of (some) DNA damage response, detection of DNA damage.
* map summary: Roche_cvt: RCV_000006; class_expression 3790BC15-33E1-4D0D-B7F4-1A3B05BC4DBC some GO_0042769; manual_list_count 41, generated_list_count 9
* [Results](DNA_damage_RCV_000006.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/38)
* Status: open

#### DNA replication RCV_000010
* Key class: [DNA replication](http://www.ebi.ac.uk/ontology-lookup/?termId=GO:0006260)
* Pattern: [is_a_OR_part_of_OR_regulates](../../patterns/is_a_OR_part_of_OR_regulates.md)
* Definition: DNA replication OR a part of DNA replication OR a process that regulates DNA replication
* map summary: Roche_cvt: RCV_000010; class_expression 1C127FE1-B049-4E09-8DCC-8B323644160F some GO_0006260; manual_list_count 43, generated_list_count 163
* [Results](DNA_replication_RCV_000010.tsv)
* [Ticket](https://github.com/GO-ROCHE-COLLAB/Roche_CV_mapping/issues/59)
* Status: closed

