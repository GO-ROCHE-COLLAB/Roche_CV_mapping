#!/usr/bin/env python
import sys
import re

def tsv2md(line):
    return "|" + re.sub("\t", "|", line) + "|"

tsv_file = open(sys.argv[1], "r")

tsv = []
for line in tsv_file:
    tsv.append(line.rstrip("\n"))

col_num = len(tsv[0].split("\t"))

print (tsv2md(tsv.pop(0)))
print "|" + ("---|" * col_num)

for line in tsv:
    print tsv2md(line)

