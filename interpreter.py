#!/usr/bin/env python
import sys
import re

path = sys.argv[3]
import os
try: 
    os.makedirs(path)
except OSError:
    if not os.path.isdir(path):
        raise

rna = open(sys.argv[1], "r").read()
translation = open(sys.argv[2], "r").read()

start = "AUG"
end = ["UAG", "UAA", "UGA"]
table = []
for a in "ACGU":
  for b in "ACGU":
    for c in "ACGU":
      table.append(a+b+c)
table.remove(start)
for i in end:
  table.remove(i)

d = dict()
for i in range(len(table)):
  if i<len(translation):
    d[table[i]]=translation[i]
  else:
    d[table[i]]=""
d[start] = ""
for i in end:
  d[i] = ""

index = 0
for x in re.finditer( r'(?=AUG((...)*?)(UAG|UAA|UGA))', rna):
  f = open(path+"/"+str(index),"w")
  for y in re.finditer(r'...', x.group(1)):
    f.write(d[y.group()])
  f.close()
  index=index+1
