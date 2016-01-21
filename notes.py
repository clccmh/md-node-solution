import argparse, fnmatch, os, webbrowser, markdown

parser = argparse.ArgumentParser(description='Actions for notes')
parser.add_argument('string', type=str, nargs="+", action='store', help='a string to search for')
parser.add_argument('-u', action='store_true', help='Update the file db')
parser.add_argument('-t', action='store_true', help='Search through the tag, or the description (faster)')
args = parser.parse_args()

def handleSelection(options):
    for x in range(0, len(options)):
        options = options[x].split(',')
        print("%d) %s: %s" % (x, options[1], options[2]))
    choice = raw_input("Select the number you want to view, or q to quit: ")
    if choice != 'q':
        choice = int(choice)
        with open(options[choice], "r") as f:
            with open("temp.html", "w") as o:
                o.seek(0)
                o.truncate()
                text = ""
                for line in f:
                    if line[0] != "/":
                        text += line
                o.write(markdown.markdown(text))
                webbrowser.open_new(os.path.abspath("temp.html"))

if args.t:
    print(args)
    options = []
    with open("files.conf", "r") as f:
        for line in f:
            if all (x in line for x in args.string):
                options.append(line)
    handleSelection(options)

if args.u:
    #Open our file, and remove everything from it
    out = open("files.conf", "w")
    out.seek(0)
    out.truncate()
    for root, dirnames, filenames in os.walk('files'):
        for filename in fnmatch.filter(filenames, '*.md'):
            filename = os.path.join(root, filename)
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


