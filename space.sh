#!/bin/bash

pwd > this_space.log
du -h | sort -h -r >> this_space.log
head -17 this_space.log
