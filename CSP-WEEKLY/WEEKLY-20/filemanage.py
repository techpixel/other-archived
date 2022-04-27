import toml, csv

def quickDump(filename, contents):
    with open(filename, "w+") as f:
        f.write(str(contents))

def configwrite(contents):
    with open("config.toml", "w+") as f:
        f.write(toml.dumps(contents))
        
def openconfig():
    with open("config.toml", "r+") as f:
        return toml.loads(f.read())

def tablecsv(filename):
    with open(filename, newline='') as csvfile:
        tablecsv = csv.reader(csvfile, delimiter=',', quotechar='|')
        
        lines = []
        for line in tablecsv:
            lines.append(list(map(int, line)))
        return lines

def dumptable(filename, contents):
    with open(filename, 'w') as csvfile:
        tablewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in contents:
            tablewriter.writerow(row)