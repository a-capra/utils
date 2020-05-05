import fnmatch
import os
import sys

for file in os.listdir(sys.argv[1]):
    if fnmatch.fnmatch(file, sys.argv[2]):
        print(os.path.abspath(file))
