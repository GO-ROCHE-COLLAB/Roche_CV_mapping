import glob
from tsv2pdm import tab

results_files = glob.glob("*RCV_*.tsv")
results_files.append("results_template.tsv")

for r in results_files:
    t = tab("", r)
    t.append_column("is_obsolete", 0)
    f = open(r, "w")
    f.write(t.print_tab())
    f.close()