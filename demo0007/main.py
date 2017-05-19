import re

def findCodes():
    codes = 0
    spaces = 0
    notes = 0

    with open('demo0007/demo.m', 'r') as f:
        for line in f.readlines():
            if line == '\n':
                spaces += 1
            elif re.match('\x20*//', line) != None:
                notes += 1
            else:
                codes += 1
    
    print('codes: %d\nspace: %d\nnotes: %d' % (codes, spaces, notes))
            

if __name__ == '__main__':
    findCodes()