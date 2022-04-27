import os, time, json, sys


def product(*args, repeat=1, allowMultideChars=False):
    # directly taken from the python docs (did modify it)
    # would use itertools, but it causes repl to die
    # built in repeat detection

    pools = [tuple(pool) for pool in args] * repeat
    result = ['']
    for pool in pools:
        result = [x + y for x in result for y in pool]
    for prod in result:
        if not len(set(prod)) == len(list(prod)) and not allowMultideChars:
            continue
        print(f"Loaded {prod}...")
        yield prod
        
def find_repeat(chars):
    seen = []
    for char in chars:
        if char in seen:
            return True
        seen.append(char)
    return False


def getAllForms(text, allowMultideChars=False):
      sort = []

      for length in range(1, len(text) + 1):
          sort.extend(
              list(
              product(text, repeat=length, allowMultideChars=allowMultideChars))
              )

      return sorted(sort)


def saveSort(name, sort):
    with open(name + '.json', 'w+') as f:
        f.write(json.dumps(sort))


def loadSort(name):
    with open(name, 'r+') as f:
        sort = json.loads(f.read())
    return sort

def direct2text(text):
  # I didn't note this as this isn't very useful as it requires post processing returning back to the issue of crashing. Plus it's also how I made thedroneone.json by writing as it goes then reindexing and then serailize it to json.

  with open('temp', 'w+') as f:
    for length in range(len(text)):
      for chars in product(text, repeat=length, allowMultideChars=False):
        basestr = ''
        for char in chars:
          basestr += char
        f.write(basestr + '\n')

def main():
    import beautify

    beautify.begin(
        getAllForms, saveSort, loadSort
    )  # "beautifies" the function for input, all the actual code is in the functions


if __name__ == '__main__':
    main()