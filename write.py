#!/usr/bin/env python

# ./write.py [rna file] [translation file] [code files...]

import sys

code = []
for f in sys.argv[3:]:
  code.append(open(f, "r").read())

letters = "".join(i for i in sorted(set("".join( j for j in code))))
if len(letters)>60:
  print "too many letters"
  print letters
  print len(letters)
  sys.exit()
  
letters_out = open(sys.argv[2], "w")
letters_out.write(letters)
letters_out.close()

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
for i in range(len(letters)):
  d[letters[i]]=table[i]

rna = open(sys.argv[1],"w")
for f in code:
  rna.write(start)
  for i in f:
    rna.write(d[i])
  rna.write(end[0])
rna.close()