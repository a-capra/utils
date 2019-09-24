import re
from sys import argv

#texfile='/home/acapra/Documents/TUG-AGM2019/ALPHA_Status_and_Prospects.tex'
texfile=argv[1]
#patt="{[^}]*.png}"
patt='{[^}]*.%s}'%argv[2]
fnames=[re.findall(patt,line) for line in open(texfile)]
for f in fnames:
    for g in f:
        print g.strip('{').strip('}')



# grep -o -e "{[^}]*.png}" ALPHA_Status_and_Prospects.tex | awk -F '{|}' '{print $2}'
