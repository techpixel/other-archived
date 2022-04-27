import importlib, sys, os, traceback
import matchpy

def error(name, reason):
    print(f"\033[38;5;196m[{name}]\033[0m {reason}")

def infopr(name, reason):
    print(f"\033[38;5;27m[{name}]\033[0m {reason}")

def test(filename):
    try:
        importlib.import_module(filename)
    except ModuleNotFoundError as e:
        if filename not in os.listdir():
            error("FILE_DOESNOT_EXIST",
            """
The file you are attempting to test for does not
exist.
            """)
        else:
            error("ER01",
            """
The module you attempted to import failed to import.
            """)
            infopr("INF01",
            """
You tried to import a module that doesn't exist.
Create a new file or fix the typo.
            """)
            if input("Would you like the traceback?").lower()[0] == 'y':
                os.system('clear')
                print("Printing Traceback for Debugging Information\033[38;5;196m")
                traceback.print_exc()
                print("\033[0m-- END TRACEBACK --")

    except BaseException as exception:
        matchException(exception)

def info():
    print(f"""

#WEEKLY 21 Pytest Information and Help

Active Owner: {os.environ["REPL_OWNER"]}
Current Working Directory: {os.getcwd()}
Is fork: {'no' if os.environ["REPL_OWNER"] == 'HarperframeInc' else 'yes'}

For help Information use 'python main.py help'

    """)

def helpfunc():
    print("""
    
#WEEKLY 21 Pytest Help

Commands:
'python main.py help' - Brings Up this Menu
'python main.py test <filename>' - Launches test menu
'python main.py info' | 'python main.py' - Opens the Info Page
'python main.py search <query>' - Experimental Search Feature
'python main.py manual <code>' - Get exit code reason
'python tutorial.py' - external program to open python tutorial

For more Information, look at the info page

    """)

def main():
    try:
        function = sys.argv[1]
    except IndexError:
        info()

    if function == 'test':
        try:
            test(sys.argv[2])
        except IndexError:
            print("Missing Argument")
    elif function == 'search':
        print(' '.join(sys.argv[2:]))
    elif function == 'help':
        helpfunc()
    elif function == 'info':
        info()
    elif function == 'manual':
        answerMatch(sys.argv[2:])
    else:
        info()

if __name__ == '__main__':
    main()