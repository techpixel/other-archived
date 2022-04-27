class TimesTable:
    def __init__(self, r, c):
        self.row = r + 1
        self.col = c + 1
    
    def generateTable(self):
        table = []

        for i in range(1, self.row):
            table.append([i * v for v in range(1, self.col)])

        return Table(*table)

    def speedTable(self):
        distinctSorts = []

        for i in range(1, self.row):
            for v in range(1, self.col):
                if not i*v in distinctSorts:
                    yield i*v
                    distinctSorts.append(i*v)
    
    def getTableInstance(table): #instead of rewriting entirety of code, make a function that gives us a table instance
        return Table(*table)

class Table:
    def __init__(self, *table):
        self.table = table
    
    def locate(self, x, y):
        return self.table[x-1][y-1]

    def pprint(self):
        for row in self.table:
            for item in row:
                print(str(item).rjust(5), end=' ')
            print('')

    def getDistinct(self):
        distintctValues = []

        for row in self.table:
            for item in row:
                if item in distintctValues:
                    pass
                else:
                    distintctValues.append(item)

        return sorted(distintctValues)

def main():
    import beautify #ngl on this one, there is important functionality here. The core is in this file.

    beautify.display(TimesTable)

if __name__ == '__main__':
    main()