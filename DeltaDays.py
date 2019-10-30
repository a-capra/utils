#!/usr/bin/env python3

from datetime import date
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("year1",type=int)
parser.add_argument("month1",type=int)
parser.add_argument("day1",type=int)

parser.add_argument("year2",type=int)
parser.add_argument("month2",type=int)
parser.add_argument("day2",type=int)

args = parser.parse_args()

d1 = date(args.year1, args.month1, args.day1)
d2 = date(args.year2, args.month2, args.day2)
delta = d2 - d1
print( delta.days+1, "days")
