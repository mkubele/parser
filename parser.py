import sys
from datetime import datetime

file = sys.argv[1]
arg = sys.argv[2]
cont = None

def parser():
    if file.lower().endswith('.txt'):
        if arg == '-s':
            start = None
            end = None
            format = "%m-%d %H:%M:%S.%f"

            with open(file, 'r') as fl:
                for line in fl:
                    if 'TEST STARTED' in line:
                        start = line
                        start = datetime.strptime(start[:18], format)
                    if 'TEST FINISHED' in line:
                        end = line
                        end = datetime.strptime(end[:18], format)
                if start is not None or end is not None:
                    dur = end - start
                else:
                    sys.exit('no test run found')
                print(dur)

        elif arg == '-i':
            cont = sys.argv[3]
            cont = cont.split(',')

            with open(file, 'r') as fl:
                for line in fl:
                    if all(value in line for value in cont):
                        print(line)

        elif arg == '-e':
            cont = sys.argv[3]
            cont = cont.split(',')

            with open(file, 'r') as fl:
                for line in fl:
                    if not any(value in line for value in cont):
                        print(line)

        elif arg == '-h':
            print(
                '-h  prints out help containing info about all available switches\n\
-s prints out the time difference between lines containing “TEST STARTED” and “TEST FINISHED”\n\
-i <args,…> prints out lines containing all arguments\n\
-e <args,…> prints out all lines which don\'t contain any of provided arguments')
            sys.exit(0)

        else:
            sys.exit('unknown argument')

    else:
            sys.exit('not a txt file')

parser()