#!/usr/bin/env python
import sys
import os

# Configure your favorite diff program here.
#DIFF = "/usr/local/bin/my-diff-tool"
DIFF = "/usr/bin/diffuse"

# Subversion provides the paths we need as the last two parameters.
LEFT  = sys.argv[-2]
RIGHT = sys.argv[-1]

# Call the diff command (change the following line to make sense for
# your diff program).
#cmd = [DIFF, '--left', LEFT, '--right', RIGHT]
cmd = [DIFF, LEFT, RIGHT]
os.execv(cmd[0], cmd)

# Return an errorcode of 0 if no differences were detected, 1 if some were.
# Any other errorcode will be treated as fatal.
