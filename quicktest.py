import argparse
import glob

parser = argparse.ArgumentParser(description='Actions for notes')
parser.add_argument('-u', action='store_true', help='Update the file db')
args = parser.parse_args()

if args.u:
    for filename in glob.glob('*.md'):
        print(filename)
        f = open(filename, "r")
        if f.readline(1) == "{":
            for line in f:
                if line == "}":
                    continue
                print(line)


