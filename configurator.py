import json
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('model', type=argparse.FileType('r'),help="")
#parser.add_argument('path', nargs='+', help="")
parser.add_argument('newvalue', help="")
parser.add_argument("-o", "--output", type=str,help="")
args = parser.parse_args()

data = json.load(args.model)

if data['Filter']['Name'] == "Moving Average":
    data['Filter']['Par0'] = args.newvalue

if args.output is None:
    foutname="output.json"
else:
    foutname=args.output

with open(foutname, 'w') as fout:
    json.dump(data, fout, indent=4)
