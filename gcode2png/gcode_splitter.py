#!/usr/bin/python3

import sys, os

def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', sys.argv)

    fname = sys.argv[1]
    path = sys.argv[1].split('.')[0]
    print(path)
    
    if not os.path.exists(path):
        os.mkdir(path)
    print(os.path.exists(path))
    if path[-1] != '/':
        path += '/'
    
    f = open(fname, 'r', encoding="utf8")
    bStart = False
    lData = []
    
    for x in f.readlines():
        if bStart is False and x.find('LAYER:') != -1:
            bStart = True
            data = ''
        elif bStart is True and x.find('LAYER:') != -1:
            lData.append(data)
            data = ''
        elif bStart is True:
            data += x
    lData.append(data)
    for i in range(len(lData)):
        strLayer = str(i+1).zfill(3)
        ff = open(path+strLayer+'.gcode', 'w', encoding="utf8")
        ff.write(lData[i])

if __name__ == '__main__':
    main()
