#!/usr/bin/env python2
# txtscroll.py

from sys import argv

# Constants
gamedir = '%s/' % argv[1]

# Init
currentfile = gamedir + 'menu.txts'

# Game
while True:
    choices = []
    choicenum = 1
    cf = open(currentfile, 'r')
    for line in cf:
        line = line.strip()
        line = line.split('#')[0]
        if not line: continue
        if line.startswith('|=') and line.endswith('=|'):
            line = line.strip('|').strip('=')
            print '\033[1m' + line.center(80) + '\033[0m'
        elif line.startswith('@'):
            line = line.split('@')[1]
            choices.append(gamedir + line.split(':')[0])
            line = line.split(':')[1]
            print '%i: %s' % (choicenum, line)
            choicenum += 1
        else:
            print line

    choice = int(raw_input('Choice: '))
    if choice == 0:
        print 'Invalid choice'
        continue
    try:
        currentfile = choices[choice-1]
        if currentfile == gamedir + '$quit$':
            exit()
    except IndexError:
        print 'Invalid choice'

    cf.close()
