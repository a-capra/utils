import fnmatch
import os
import sys

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, sys.argv[1]):
        print(os.path.abspath(file))
