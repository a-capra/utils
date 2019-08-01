# alias git-url="python3 $HOME/_scripts/git-url.py"
# alias git-url="python3 $HOME/utils/git-url.py"

from pathlib import Path
import sys

if not Path('./.git').is_dir():
    sys.exit('not a git repo')

with open('./.git/config','r') as conf:
    for line in conf:
        if line.strip() == '[remote "origin"]':
            print(next(conf).strip()[6:])
            sys.exit(0)            

