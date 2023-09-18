from sys import path
path.insert(0, './start')
from start.start_ping import start 

def main():
  while True:
    start()

if __name__ == "__main__":
  main()
input('Press ENTER to exit')