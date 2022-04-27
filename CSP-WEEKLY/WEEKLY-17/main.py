#
#WEEKLY 17
#
#

import threading, time, os

active = True

def listen():
  global active
  #FibboIn = open('input.fib', 'r+')
  #FibboOut = open('output.fib', 'w+')
  
  print("[\033[1m\033[38;5;34mLISTENER\033[0m] Beginning Process")

  with open('input.fib', 'r+') as FibboIn:
    last_saved_output = FibboIn.readlines()[-1]
  print("[\033[1m\033[38;5;34mLISTENER\033[0m] Got last saved output")

  with open('output.fib', 'w+') as FibboOut:
    FibboOut.write('0\n1')
  print("[\033[1m\033[38;5;34mLISTENER\033[0m] Updated Output")

  while active == True:
      time.sleep(0.25) #interval
      with open('input.fib', 'r+') as FibboIn:
        if int(FibboIn.readlines()[-1]) != int(last_saved_output):
          
          FibboIn.seek(0, 0)
          last_saved_output = FibboIn.readlines()[-1]
          print(f"[\033[1m\033[38;5;34mLISTENER\033[0m] Match: {last_saved_output}")
          print(f"[\033[1m\033[38;5;34mLISTENER\033[0m] Updated Last Saved Output")

          with open('output.fib', 'a+') as FibboOut:
            FibboOut.seek(0, 0)
            last_term = int(FibboOut.readlines()[-1])
            FibboOut.seek(0, 0)
            slast_term = int(FibboOut.readlines()[-2])
            FibboOut.write('\n' + str(last_term + slast_term))
          
            print(f"[\033[1m\033[38;5;34mLISTENER\033[0m] Updated Fibbonaci")
        else:
          print(f"[\033[1m\033[38;5;160mLISTENER\033[0m] No Match: {last_saved_output}")
  print("\033[1mPROCESS ENDED\033[0m: LISTENER")

def main(num):
  global active
  print("[\033[1m\033[38;5;27mMAIN\033[0m] Beginning Process")

  with open('input.fib', 'a+') as FibboIn:
    FibboIn.write("0")

  time.sleep(1)

  for num in range(1, num):
    print(f"[\033[1m\033[38;5;27mMAIN\033[0m] Updating Input {str(num)}")
    time.sleep(0.5) #interval; make slower to let listener catch up
    with open('input.fib', 'a+') as FibboIn:
      FibboIn.write('\n' + str(num))

  print("[\033[1m\033[38;5;27mMAIN\033[0m] Processes finished - Ending Processes")
  active = False
  print("\033[1mPROCESS ENDED\033[0m: MAIN")

if __name__ == '__main__':
  threadmain = threading.Thread(target=main, args=[int(input("\033[1mEnter a number:\033[0m "))])
  threadmain.start()
  print("[\033[1m\033[38;5;27mMAIN\033[0m] Starting Listner Process")
  
  listener = threading.Thread(target=listen)
  listener.start()

  os.system('clear')  

  while threadmain.is_alive() or listener.is_alive(): pass

  os.system('clear')
  result = open('output.fib', 'r+').readlines()[-1]
  print("\033[1mResult:\033[0m " + result)

  resetcontents = input("Would you like to \033[38;5;220mreset file contents\033[0m? [Y\\N]")

  if resetcontents.lower() == 'y': #resets contents for next time
    open('input.fib', 'w+').close()
    open('output.fib', 'w+').close()
  else:
    print("Did not reset file contents. Make sure to clear the file's contents before you exit.")