import getch, os, filemanage, sys

assets = {
    "welcome":
    """
  \033[38;5;164mTimes Table Tool\033[0;0m
  
  Do you need to find the distinct values on a times table,
  but are too lazy to do it yourself? I don't but I'm su-
  Whatever. Let's get to the point of things.

  This tool generates a Times Table and provides useful functions,
  however it focuses on distinct values of the time table.

  If you want fast results, use speeed mode.

  \033[7m<NEXT>\033[0m 
  """,
    "select": [
        """
  \033[38;5;164mTimes Table Tool\033[0;0m
  
  Well you haven't closed out the program. That's good.
  Use speeed mode if you want a direct dump of the table or
  distinct values.
  I suggest using normal mode. It sets up your table and allows
  you to manage multiple tables.
 
  If you don't have a working TTT directory, you will be sent
  to setup.

  \033[7m<NORMAL>\033[0m <SPEEED>
  """, """
  \033[38;5;164mTimes Table Tool\033[0;0m
  
  Well you haven't closed out the program. That's good.
  Use speeed mode if you want a direct dump of the table or
  distinct values.
  I suggest using normal mode. It sets up your table and allows
  you to manage multiple tables.
 
  If you don't have a working TTT directory, you will be sent
  to setup.

  <NORMAL> \033[7m<SPEEED>\033[0m
  """
    ]
}


def nav(asset):
    index = 0
    while True:
        os.system('clear')
        print(asset[index])
        key = getch.getch()
        if key.lower() == 'a':
            index -= 1
            if index < 0:
                index += 1
        elif key.lower() == 'd':
            index += 1
            if index == len(asset):
                index -= 1
        else:
            return index


def fnav(asset, contents):
    index = 0
    while True:
        os.system('clear')
        print(asset.format(contents[index]))
        key = getch.getch()
        if key.lower() == 'a':
            index -= 1
            if index < 0:
                index += 1
        elif key.lower() == 'd':
            index += 1
            if index == len(contents):
                index -= 1
        else:
            return contents[index]


def bnav(asset, func):
    index = 0
    while True:
        os.system('clear')

        func()
        print(asset[index])

        key = getch.getch()
        if key.lower() == 'a':
            index -= 1
            if index < 0:
                index += 1
        elif key.lower() == 'd':
            index += 1
            if index == len(asset):
                index -= 1
        else:
            return index

def fbnav(asset, func, formatter):
    index = 0
    while True:
        os.system('clear')

        func()
        print(asset[index].format(formatter))

        key = getch.getch()
        if key.lower() == 'a':
            index -= 1
            if index < 0:
                index += 1
        elif key.lower() == 'd':
            index += 1
            if index == len(asset):
                index -= 1
        else:
            return index

def printgetch(asset):
    print(asset)
    getch.getch()
    os.system('clear')


def display(TimesTable):
    printgetch(assets["welcome"])
    mode = nav(assets["select"])

    if mode == 1:
        speedDump(TimesTable)
        return

    if os.path.exists("TTTWorkspace"):
        openWorkspace(TimesTable)
    else:
        setupWorkspace(TimesTable)


def speedDump(TimesTable):
    os.system('clear')

    print("\033[38;5;208mWarning\033[0m")
    print("Before you proceed, make sure that TTT.txt is renamed")
    print("or deleted. Speeed will truncate the file.")
    getch.getch()

    r = input("\033[38;5;164mNumber of Rows \033[38;5;93m[3]\033[0m: ")
    c = input("\033[38;5;164mNumber of Columns \033[38;5;93m[3]\033[0m: ")

    if not r.isnumeric():
        print("Defaulting Rows")
        r = 3
    if not c.isnumeric():
        print("Defaulting Columns")
        c = 3

    table = TimesTable(int(r), int(c))

    print("\033[38;5;34mBuilt Times Table\033[0m")
    print("\033[38;5;34mDumping to TTT.txt\033[0m")

    try:
        filemanage.quickDump("TTT.txt", [*table.speedTable()])
    except:
        print("\033[38;5;196mError while writing.\033[0m")
        sys.exit(1)
    else:
        sys.exit()


def setupWorkspace(TimesTable):
    os.mkdir("TTTWorkspace")
    os.chdir("TTTWorkspace")

    print("\033[38;5;34mSetting up your workspace.\033[0m")

    config = {
        "base": {
            "reserved": ["config.toml", "readme.txt"],
            "files": ["welcome.csv"],
        },
        "personalization": {
            "view": "cozy"
        }
    }
    readme = """
    Thanks for using TTTWorkspace.
    To provide a bugfree experience, do not modify the contents
    of this directory and subdirectories.
    """
    welcome = """1,2,3
2,4,6
3,6,9"""

    try:
        filemanage.configwrite(config)
        filemanage.quickDump("readme.txt", readme)
        filemanage.quickDump("welcome.csv", welcome)
    except:
        print("\033[38;5;196mError while setting up your workspace.\033[0m")
        sys.exit(1)
    else:
        print("\033[38;5;34mSucess!\033[0m")

    os.chdir("..")

    openWorkspace(TimesTable)


def openWorkspace(TimesTable):
    os.chdir("TTTWorkspace")
    tomlconfig = filemanage.openconfig()

    if tomlconfig["personalization"]["view"] == "compact":
        os.chdir("..")
        Compact.openWorkspace(TimesTable)
    if tomlconfig["personalization"]["view"] == "cozy":
        os.chdir("..")
        Cozy.openWorkspace(TimesTable)


class Compact:
    def openWorkspace(TimesTable):
        os.chdir("TTTWorkspace")

        while True:
            os.system('clear')
            tomlconfig = filemanage.openconfig()

            print('manager')
            for file in tomlconfig["base"]["files"]:
                print(file)

            print("\n\033[1m\033[38;5;164mTTTWorkspace\033[0m")
            print("Choose a file to open. Cannot open reserved files.")

            while True:
                filename = input(">")
                if filename in tomlconfig["base"]["files"]:
                    break
                elif filename == 'manager':
                    Compact.workspaceManager(TimesTable)
                else:
                    print("Not a valid file.")

            os.system('clear')

            table = TimesTable.getTableInstance(filemanage.tablecsv(filename))

            Compact.tableManager(TimesTable, table)

    def tableManager(TimesTable, table):
        while True:
            os.system('clear')
            table.pprint()
            print("\n\033[1m\033[38;5;164mTTTWorkspace\033[0m")
            print("Choose an option:")
            print("1 - Export")
            print("2 - Distinct Values")
            print("3 - Back")
            key = getch.getch()

            if key == '1':
                while True:
                    os.system('clear')
                    print("Choose a format:")
                    print("1 - JSON")
                    print("2 - CSV")
                    print("3 - Python Importable")

                    key = getch.getch()
                    if key == "1":
                        import json
                        os.chdir("..")
                        tablejson = json.dumps(table.table)
                        filemanage.quickDump("TTTExport.json", tablejson)
                        print("Sucess")
                        sys.exit()
                    elif key == "2":
                        os.chdir('..')
                        filemanage.dumptable("TTTExport.csv", table.table)
                        print("Sucess")
                        sys.exit()
                    elif key == "3":
                        script = "table = " + str(table.table)
                        os.chdir("..")
                        with open("TTTExport.py", "w+") as f:
                            f.write(script)
                        print("Sucess")
                        sys.exit()
                    else:
                        print("Invalid Character")
            elif key == '2':
                os.system('clear')
                distinctValues = table.getDistinct()
                for i in distinctValues:
                    print(i, end='  ')
                print('')

                print(f"There are {len(distinctValues)} distinct values")
                getch.getch()
            elif key == '3':
                return
            else:
                print("Invalid Character")

    def workspaceManager(TimesTable):
        os.system('clear')
        tomlconfig = filemanage.openconfig()

        while True:
            os.system('clear')

            for file in tomlconfig["base"]["files"]:
                print(file)

            print("\n\033[1m\033[38;5;164mTTTWorkspace\033[0m")
            print("Choose an option:")
            print("1 - Create a Times Table")
            print("2 - Delete Times Table")
            print("3 - Back")

            key = getch.getch()

            if key == '1':
                r = input("Enter number of rows >")
                c = input("Enter number of columns >")

                if not r.isnumeric():
                    print("Defaulting Rows to 3")
                    r = 3
                if not c.isnumeric():
                    print("Defaulting Columns to 3")

                print("Created your times table")

                table = TimesTable(int(r), int(c)).generateTable()

                filename = input("CSV Name > ") + ".csv"

                filemanage.dumptable(filename, table.table)

                config = filemanage.openconfig()

                config["base"]["files"].append(filename)

                filemanage.configwrite(config)

                print("Config Updated....sucess")
                getch.getch()
                return
            elif key == '2':
                filename = input(
                    "Enter a file to delete (excluding manager) >")

                config = filemanage.openconfig()

                if filename in config["base"]["files"]:
                    os.remove(filename)
                else:
                    return

                config["base"]["files"].remove(filename)

                filemanage.configwrite(config)

                print("Config Updated....sucess")
                getch.getch()
                return
            elif key == '3':
                return


cozyAssets = {
    "filechoose":
    """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Select the table/tool you want to use.


    \033[7m<    {}    >\033[0m
    Use the WASD and Enter keys to control the menu


    \033[7m<ENTER>\033[0m
    """,
    "tablemenu": [
        """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Export, Get Distinct Values, or Exit

    \033[7m<DISTINCT VALUES>\033[0m <EXPORT> <EXIT>
    """, """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Export, Get Distinct Values, or Exit

    <DISTINCT VALUES> \033[7m<EXPORT>\033[0m <EXIT>
    """, """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Export, Get Distinct Values, or Exit

    <DISTINCT VALUES> <EXPORT> \033[7m<EXIT>\033[0m
    """
    ],
    "exportmenu": [
    """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Choose a file type or exit.

    \033[7m<JSON>\033[0m <CSV> <EXIT>
    """, """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Choose a file type or exit.

    <JSON> \033[7m<CSV>\033[0m <EXIT>
    """, """
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Choose a file type or exit.

    <JSON> <CSV> \033[7m<EXIT>\033[0m
    """
    ],
    "managermenu":["""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Welcome to the manager! Here you can create and delete
    Times Tables!

    Create a custom times table using the Create button.
    Delete times tables with the Delete button.
    Otherwise use the Return button to return to the main menu.

    \033[7m<CREATE>\033[0m <DELETE> <EXIT>
    ""","""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Welcome to the manager! Here you can create and delete
    Times Tables!

    Create a custom times table using the Create button.
    Delete times tables with the Delete button.
    Otherwise use the Return button to return to the main menu.

    <CREATE> \033[7m<DELETE>\033[0m <EXIT>
    ""","""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Welcome to the manager! Here you can create and delete
    Times Tables!

    Create a custom times table using the Create button.
    Delete times tables with the Delete button.
    Otherwise use the Return button to return to the main menu.

    <CREATE> <DELETE> \033[7m<EXIT>\033[0m 
    """],
    "tablewizard":"""
    \033[38;5;223mTTTWizard\033[0;0m
    
    Create a Times Table! This Wizard lets you create
    a new Times Table.
    
    This will ask you to input the amount of rows and columns
    you want
    
    Be warned that it will take time for long tables.
    

    \033[7m<NEXT>\033[0m 
    """, "tablewizardRows":"""
    \033[38;5;223mTTTWizard\033[0;0m
    
    Enter amount of rows you want.
    Must be integer.
    


    

    

    \033[7m<ROWS>\033[0m """, 
    "tablewizardCols":"""
    \033[38;5;223mTTTWizard\033[0;0m
    
    Enter amount of columns you want.
    Must be integer.
    


    

    

    \033[7m<COLUMNS>\033[0m """, 
    "tablewizardName":"""
    \033[38;5;223mTTTWizard\033[0;0m
    
    Name your table. It will automatically
    add .csv to the filename so don't worry.
    


    

    

    \033[7m<NAME>\033[0m """, 
    "tablewizardComplete":"""
    \033[38;5;223mTTTWizard\033[0;0m
    
    Sucess! Your Table should appear.
    If not, restart the program and check config.toml
    


    

    

    \033[7m<EXIT>\033[0m 
    """, "selectDel":"""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    Select the file you want to delete.


    \033[7m<    {}    >\033[0m
    Use the WASD and Enter keys to control the menu


    \033[7m<ENTER>\033[0m
    """, "setFilename":"""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m
    
    Name your file. It will automatically add
    the file extension
    


    

    

    \033[7m<NAME>\033[0m """,
    "distinctManager":["""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m

    There are {} distinct values.

    Save these distinct values as JSON,
    or go back.


    \033[7m<SAVE>\033[0m <EXIT>
    ""","""
    \033[1m\033[38;5;164mTTTWorkspace\033[0m

    There are {} distinct values.

    Save these distinct values as JSON,
    or go back.


    <SAVE> \033[7m<EXIT>\033[0m 
    """]
}


class Cozy:
    def openWorkspace(TimesTable):
        os.chdir("TTTWorkspace")

        while True:
            config = filemanage.openconfig()
            
            filename = fnav(cozyAssets["filechoose"],
                            ["manage", "exit"] + config["base"]["files"])

            if filename == 'manage':
                Cozy.workspaceManager(TimesTable)
            elif filename == 'exit':
                os.system('clear')
                print("Thanks for using TTTWorkspace")
                sys.exit()
            else:
                table = TimesTable.getTableInstance(
                filemanage.tablecsv(filename))

                Cozy.tableManager(TimesTable, table)

    def tableManager(TimesTable, table):
        while True:
            key = bnav(cozyAssets["tablemenu"], table.pprint)

            if key == 0:
                os.system('clear')
                distinctValues = table.getDistinct()

                def printval():
                    print("    ", end='')
                    for i in distinctValues:
                        print(i, end='  ')
                    print('\n')

                distinctSave = fbnav(cozyAssets["distinctManager"], printval, str(len(distinctValues)))

                if distinctSave == 0:
                    import json
                    
                    os.chdir("..")

                    distinctJson = json.dumps(distinctValues)
                    
                    while True:
                        os.system('clear')
                        print(cozyAssets["setFilename"], end='')
                        filename = input()
                        if filename.isalnum():
                            filename += ".json"
                            break

                    filemanage.quickDump(filename, distinctJson)
                    os.chdir("TTTWorkspace")
                else:
                    continue
            if key == 1:
                exporttype = nav(cozyAssets["exportmenu"])

                if exporttype == 0:
                    import json

                    os.chdir("..")

                    tablejson = json.dumps(table.table)

                    while True:
                        os.system('clear')
                        print(cozyAssets["setFilename"], end='')
                        filename = input()
                        if filename.isalnum():
                            filename += ".json"
                            break

                    filemanage.quickDump(filename, tablejson)
                    os.chdir("TTTWorkspace")

                elif exporttype == 1:
                    os.chdir('..')

                    while True:
                        os.system('clear')
                        print(cozyAssets["setFilename"], end='')
                        filename = input()
                        if filename.isalnum():
                            filename += ".csv"
                            break

                    filemanage.dumptable(filename, table.table)

                    os.chdir("TTTWorkspace")
                elif exporttype == 2:
                    pass
            if key == 2:
                return

    def workspaceManager(TimesTable):
        while True:
            key = nav(cozyAssets["managermenu"])

            if key == 0:
                os.system('clear')
                printgetch(cozyAssets["tablewizard"])
                
                while True:
                    os.system('clear')
                    print(cozyAssets["tablewizardRows"], end='')
                    r = input()
                    if r.isnumeric():
                        r = int(r)
                        break
                while True:
                    os.system('clear')
                    print(cozyAssets["tablewizardCols"], end='')
                    c = input()
                    if c.isnumeric():
                        c = int(c)
                        break

                table = TimesTable(r, c).generateTable()
                
                while True:
                    os.system('clear')
                    print(cozyAssets["tablewizardName"], end='')
                    filename = input()
                    if filename.isalnum():
                        filename +=".csv"
                        break
                
                filemanage.dumptable(filename, table.table)

                config = filemanage.openconfig()

                config["base"]["files"].append(filename)

                filemanage.configwrite(config)
            elif key == 1:
                config = filemanage.openconfig()
            
                filename = fnav(cozyAssets["selectDel"],
                            ["cancel"] + config["base"]["files"])
                
                if filename == "cancel":
                    continue
                
                config["base"]["files"].remove(filename)

                filemanage.configwrite(config)
            elif key == 2:
                return