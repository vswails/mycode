#!/usr/bin/env python3

varzach = "Zach the python instructor"

varfileread = open('/tmp/log.vzw', "r")
varfilewrite = open('/tmp/logparsed.vzw', "w")

templist = varfileread.readlines()

for x in templist:         ## first time through loop, x is first line in varfileread; 2nd time is 2nd line, etc.)
  print(x, end=' ')

  if "User-Agent:"  in x:
    print(x)

varfileread.close()
varfilewrite.close()




varfile1 = open('doritos.dat', 'w')

print('jason gave this line', file=varfile1)
print('here is a second line into the file', file=varfile1)
print(varzach, file=varfile1)

varfile1.close()

