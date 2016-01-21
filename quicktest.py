import argparse
import glob
import os

parser = argparse.ArgumentParser(description='Actions for notes')
parser.add_argument('-u', action='store_true', help='Update the file db')
args = parser.parse_args()

if args.u:
    #Open our file, and remove everything from it
    out = open("files.conf", "w")
    out.seek(0)
    out.truncate()
    for filename in glob.glob('*.md'):
        print(filename)
        title = ""
        description = ""
        tags = ""
        f = open(filename, "r")
        for line in f:
            if line[0] == "/" and line[1] == "/":
                fline = line.strip("//").split(" ")
                if fline[0] == "Title:": title = fline[1].strip("\n")
                if fline[0] == "Description:": description = ' '.join(fline[1:]).strip("\n")
                if fline[0] == "Tags:": tags = ''.join(fline[1:]).strip('\n')
        out.write(os.path.abspath(filename) + ',' + title + ',' + description + ',' + tags + '\n')
