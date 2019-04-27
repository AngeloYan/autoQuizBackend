#!/bin/sh/python

import wptools
import sys
import re

topic = sys.argv[1]
so = wptools.page(topic).get_parse()
print("\n\n")
for i in so.data['infobox']:
    print(i,end="")
    print(so.data['infobox'][i])

# Question on DoB
if 'birth_date' in so.data['infobox']:
    dat = so.data['infobox']['birth_date']
    DoB = re.search(r"\d{4}\|\d{1,2}\|\d{1,2}",dat).group().split('|')

    if len(DoB[1]) == 1:
        DoB[1] = "0" + DoB[1]
    if len(DoB[2]) == 1:
        DoB[2] = "0" + DoB[2]

    ans = DoB[0] + "/" + DoB[1] + "/" + DoB[2]
    print(ans)
else:
    print("No recorded Birth Date")
# Question on children
if 'children' in so.data['infobox']:
    dat = so.data['infobox']['children']
    try:
        val = int(dat)
        print(dat)
    except ValueError:
        print("No recorded children")
else:
    print("No recorded children")

# Question on nationality
if 'nationality' in so.data['infobox']:
    dat = so.data['infobox']['nationality']
    nationality = re.search("\|\w*",dat).group()
    nationality = nationality[1:]
    print(nationality)
else:
    print("No recorded nationality")

# Question on profession/occupation 