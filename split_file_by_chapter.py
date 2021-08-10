#!/usr/bin/python3

import sys

def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', sys.argv)
    
    f = open(sys.argv[1], "r", encoding="utf8")
    all_data = ""
    c=0
    state=-1
    for x in f.readlines():
        all_data += x
    f.close()
    
    x = split(["\n"], all_data)
    x = divide_chunks(x, 1000)
    print(len(x))
    print(type(x))
    f_name = split(["."], sys.argv[1])
    
    print(f_name[0] + "_1." + f_name[1])
    num=1
    for txt in x:
        f = open(f_name[0] + "_" + str(num) + "." + f_name[1], "w", encoding="utf8")
        print(type(txt))
        #print(txt)
        for t in txt:
            #print(t)
            f.writelines(t + "\n")
        num=num+1
        f.close()
        

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

def divide_chunks(l, n):      
    # looping till length l
    k = []
    for i in range(0, len(l), n): 
        k.append(l[i:i + n])
    return k

if __name__ == '__main__':
    main()
