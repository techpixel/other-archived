'''
A few CSV files have been provided for you for this assignment. Choose one to work with that interests you.
If you are able to download a dataset as a CSV file that you would like to work with instead of any of the ones provided, feel free to do so. Make sure to add your data file to this project.
'''

# 2/10/22
# Manitej Boorgu
# Data Science with Python Assignment

# Import CSV module
import csv 

# Initialize any local variables
rowIndex = 0 # Keep track of line no.
platforms = {} # Dict containg each platform and data of game
companies = {} # Dict containg each company  and data of game

# Open the CSV file - Make sure to put the entire path for the CSV file
with open('Project/Video Game Sales.csv') as csv_file:
    # Reads the cvs file and stores it as a variable
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Best Performing Game for each platform
    # Iterate through each column
    for rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, gbl_sales in csv_reader:
        if rowIndex == 0:
          rowIndex += 1
          continue # Skip first row (labels) 
        
        # Check if this is a new platform OR the sales are higher than the previous highest selling game of the platform
        if platform not in platforms.keys() or platforms[platform][1] < gbl_sales:
            platforms[platform] = [name, gbl_sales]

        rowIndex += 1

    csv_file.seek(0)
    rowIndex = 0 # Reset index
    
    # Worst Performing Game for each Game Company
    # Iterate through each column
    for rank, name, platform, year, genre, publisher, na_sales, eu_sales, jp_sales, other_sales, gbl_sales in csv_reader:
        if rowIndex == 0:
          rowIndex += 1
          continue # Skip first row (labels) 
        
        # Check if this is a new platform OR the sales are higher than the previous highest selling game of the platform
        if publisher not in companies.keys() or companies[publisher][1] > gbl_sales:
            companies[publisher] = [name, gbl_sales]

        rowIndex += 1

# Print the results

import curses # Import OS library for cleanup
import math # Mathematical calculations

stdscr = curses.initscr() # Initialize curses
curses.noecho() # Remove echo from getch

# Set body width & height
bodyMaxYX = stdscr.getmaxyx()

# Round body height & width to the nearest even number to allow divisibility by 2
bodyH = (math.floor(bodyMaxYX[0] / 2) * 2) - 2 # Leave room for footer
bodyW = math.floor(bodyMaxYX[1] / 2) * 2

# Create windows
title = curses.newwin(1, bodyW, 0, 0)
body = curses.newwin(bodyH, bodyW, 1, 0)
footer = curses.newwin(1, bodyW, bodyH + 1, 0)

# Setup title window
title.bkgd(" ", curses.A_REVERSE)
title.refresh()

# Setup footer window
footer.bkgd(" ", curses.A_REVERSE)
footer.addstr("Manitej's Game Sales Analysis - [E]Continue [W]Up [S]Down OR Scroll") 
footer.refresh()

# Generate strings suitable for curses; dynamic to window size
dispList = [
    i.ljust(10) + (platforms[i][0].ljust(bodyW - 14) if len(platforms[i][0]) < (bodyW - 17) else platforms[i][0][:(bodyW - 17)] + "...").ljust(bodyW - 14) + platforms[i][1].ljust(4) for i in platforms.keys()
] # If string length exceeds limits, add trailing periods

viewIndex = 0 # Create view index
# Set up titlebar
title.addstr("Platform".ljust(10) + "Game".ljust(bodyW - 14) + "SLS") #SLS - Sales
title.refresh()
while True: 
    body.clear() # Clear data in the body
    
    # Add updated values
    for i in range(bodyH - 1):
        body.addstr(dispList[i + viewIndex]) 

    body.refresh() # Update with new values
     
    control = body.getch() # Wait for user input

    # Go up
    if (control == ord("w") or control == ord("A")) and viewIndex > 0: # Bounds; scroll wheel support
        viewIndex -= 1

    # Go down
    elif (control == ord("s") or control == ord("B")) and viewIndex < (len(dispList) - bodyH + 1): # Bounds; scroll wheel support
        viewIndex += 1

    # Exit
    elif control == ord("e"):
        break

companiesList = list(companies.keys()) # Create new list from dict keys - dictKeys object cannot be sorted
companiesList.sort() # Sort alphabetically

# Generate new display strings; dynamic to terminal size
dispList = [
    (i.ljust((bodyW // 2) - 2) if len(i) < ((bodyW // 2) - 5) else i[:(bodyW // 2) - 5] + "...") + (companies[i][0].ljust((bodyW // 2) - 2) if len(companies[i][0]) < ((bodyW // 2) - 5) else companies[i][0][:((bodyW // 2) - 5)] + "...") + companies[i][1].ljust(4) for i in companiesList
] # If string length exceeds limits, add trailing periods

viewIndex = 0 # Reset variable
# Setup window
title.clear() # Clear the title bar
title.addstr("Publisher/Company".ljust((bodyW// 2) - 2) + "Game".ljust((bodyW // 2) - 2) + "SLS")
title.refresh()
while True: 
    body.clear() # Clear data in the body

    # Add updated values
    for i in range(bodyH - 1):
        body.addstr(dispList[i + viewIndex])

    body.refresh() # Update with new values
    
    control = body.getch() # Wait for user input

    # Go up
    if (control == ord("w") or control == ord("A")) and viewIndex > 0: # Bounds; scroll wheel support
        viewIndex -= 1

    # Go down
    elif (control == ord("s") or control == ord("B")) and viewIndex < (len(dispList) - bodyH + 1): # Bounds; scroll wheel support
        viewIndex += 1

    # Exit
    elif control == ord("e"):
        break

# End curses instance
curses.echo() # Reset curses settings
curses.endwin()