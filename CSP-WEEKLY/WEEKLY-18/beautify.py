import getch, os, random, time, copy, sys

assets = {
  "welcome": '''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  Do you need to sort a word and get the alphabetical
  positon of the scrambled version of it?
  I don't, but I'm sure you do!

  This tool has a very intuitive interface. All the
  actual sorting is in 'main.py'. The GUI stuff is
  in 'beautify.py'.

  \033[7m<NEXT>\033[0m
  ''',
  "setup": ['''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  The character sort tool can filter repeated characters
  from form matches, so forms such as "eee" and "eaa" will
  not be matched.

  Select ALLOW to filter out repeating characters (will reduce matches). 
  Select DENY to include repeating characters.


  \033[7m<ALLOW>\033[0m <DENY>
  ''','''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  The character sort tool can filter repeated characters
  from form matches, so forms such as "eee" and "eaa" will
  not be matched.

  Select ALLOW to filter out repeating characters (will reduce matches). 
  Select DENY to include repeating characters.


  <ALLOW> \033[7m<DENY>\033[0m
  '''],
  "txtin": '''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  To get started, you should enter the text you want to get
  the forms of.
  This will automatically be sorted alphabetical using ANSI
  characters code values, so capitals will have higher sort 
  priority compared to lowercase.
  You can enter a json file and the character sort tool will load it.

  ''',
  "txtinerror": '''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  To get started, you should enter the text you want to get
  the forms of.

  This will automatically be sorted alphabetical using ANSI
  characters code values, so capitals will have higher sort 
  priority compared to lowercase.
  \033[38;5;160m\033[1mError\033[0m: Please use only Alphabetical characters.
  ''',
  "waitsort":'''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  

  We are currently calculating and forming your
  sort. Please wait.




  Please wait.
  ''',
  "menu":'''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  Closest to A    Closest to Z    Top Forms      Search these
  1. {0}    1. {5}    1. {10}   1. {15}
  2. {1}    2. {6}    2. {11}   2. {16}
  3. {2}    3. {7}    3. {12}   3. {17}
  4. {3}    4. {8}    4. {13}   4. {18}
  5. {4}    5. {9}    5. {14}   5. {19}

  Search for a possible sort.
  ''',
  "sucess":'''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  

  Your sort was found sucessfully!
  Sort: {sort}
  Order: {order}



  \033[7m<NEXT>\033[0m
  ''',
  "error":'''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  

  Sort was not found.
  




  \033[7m<NEXT>\033[0m
  ''',  
  "exit": ['''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  Are you sure you want to exit?

  You may save the list as json and store it. It will
  optimize the character sort tool.
  
  If you do not want to save the character sort but exit,
  press DONT SAVE.

  \033[7m<SAVE>\033[0m <DONT SAVE> <CANCEL>
  ''','''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  Are you sure you want to exit?

  You may save the list as json and store it. It will
  optimize the character sort tool.
  
  If you do not want to save the character sort but exit,
  press DONT SAVE.

  <SAVE> \033[7m<DONT SAVE>\033[0m <CANCEL>
  ''','''
  \033[38;5;71mCharacter Sort Tool\033[0;0m
  Are you sure you want to exit?

  You may press Save to save the list as json and store it.
  It will optimize the character sort tool.
  
  If you do not want to save the character sort but exit,
  press DONT SAVE.

  <SAVE> <DONT SAVE> \033[7m<CANCEL>\033[0m
  '''],
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


def begin(getFunc, saveFunc, loadFunc):
  global assets

  print(assets['welcome'])
  getch.getch()
  os.system('clear')

  os.system('clear')
  print(assets['txtin'])
  txtin = input('  \033[7m<ENTER>\033[0m ').lower()

  usingJson = False
  if txtin.endswith('.json'):
    sort = loadFunc(txtin)
    usingJson = True
  elif not txtin.isalpha():
    while True:
      os.system('clear')
      print(assets['txtinerror'])
      txtin = input('  \033[7m<ENTER>\033[0m ')

      if txtin.isalpha():
        break

    os.system('clear')
    allowMultideChars = bool(nav(assets['setup']))
    os.system('clear')
    sort = getFunc(txtin, allowMultideChars=allowMultideChars)
    print(assets['waitsort'])
    time.sleep(random.uniform(0, 1))
    os.system('clear')
    
  else:
    os.system('clear')
    allowMultideChars = bool(nav(assets['setup']))
    os.system('clear')
    sort = getFunc(txtin, allowMultideChars=allowMultideChars)
    print(assets['waitsort'])
    time.sleep(random.uniform(0, 1))
    os.system('clear')

  rate = getRating(sort)

  while True:
    os.system('clear')
    print(assets['menu'].format(*rate))
    searchForm = input('  \033[7m<ENTER>\033[0m ')
    if searchForm in sort:
      os.system('clear')
      order = sort.index(searchForm)
      print(assets['sucess'].format(sort=sort[order], order=order))
      getch.getch()
    elif searchForm == '':
      os.system('clear')
      exittool = nav(assets['exit'])
      if exittool == 0:
        if not usingJson:
          saveFunc(txtin, sort)
        else:
          sys.exit("Process Ended: \033[0;0mSort is already saved.")
        sys.exit("Process Ended: \033[0;0mSort was saved.")
      elif exittool == 1:
        sys.exit("Process Ended: \033[0;0mDid not save sort.")
      elif exittool == 2:
        pass
    else:
      os.system('clear')
      print(assets['error'])
      getch.getch()
      
def getRating(sort):
  if len(sort) < 5:
    closeA = copy.deepcopy(sort)
    closeA += ['NONE'] * (6 - len(closeA))
    sort.reverse()
    closeZ = copy.deepcopy(sort)
    closeZ += ['NONE'] * (6 - len(closeA))
    sort.reverse()
  else:
    closeA = sort[:5]
    closeZ = sort[-5:]
    closeZ.reverse()

  for form in closeA:
    closeA[closeA.index(form)] = form + ' ' * (9 - len(form))
  for form in closeZ:
    closeZ[closeZ.index(form)] = form + ' ' * (9 - len(form))
  
  topsorts = []
  for x in range(10):
    form = random.choice(sort)
    topsorts.append(form + ' ' * (9 - len(form)))
  
  return closeA + closeZ + topsorts