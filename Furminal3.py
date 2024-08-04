import os
from pathlib import Path
from LineNumber1 import get_line

line_number = 2
Username = get_line('d.data', line_number)
if Username:
    print(f"{Username}")
    username = Username[10:]

line_number = 1
Base2 = get_line('d.data', line_number)
if Base2:
    print(f"{Base2}")
    base2 = Base2[10:]

base = base2
os.chdir(base)
print("Home directory:", base)
user = os.getlogin()
print(f"Logged in as {user}")
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"
furminal = f"{RED}{username}{BLUE}os.getcwd(){RESET}:3 "
print(f"{BLUE}Starting Furminal v0.1")
while True:
  import os
  import sys
  curdir1 = os.getcwd()
  furminal = f"{RED}{username}{BLUE}{curdir1}{RESET}:3 "
  command = input(furminal)
  com = command[:3]
  
  if command == 'quit':
    print("Quiting Furminal :3")
    sys.exit()
  if com == 'cd ':
    curdir = os.getcwd()
    if '~' in command:
      com2 = ""
    else:
      com2 = command[3:]
    os.chdir(curdir + '/' + com2)
    dir = os.getcwd()
    print(dir)
  os.system(command)
