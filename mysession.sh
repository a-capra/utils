#!/bin/bash

gnome-terminal &> /dev/null &

xclock -digital -update 1 &

nautilus $HOME &> /dev/null &

#firefox about:newtab &> /dev/null &

exit 123
