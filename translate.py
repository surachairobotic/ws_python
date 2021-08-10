#!/usr/bin/python3

import sys
from deep_translator import GoogleTranslator

def main():
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', sys.argv)
    
    f = open(sys.argv[1], "r", encoding="utf8")
    all_data = ""
    for x in f.readlines():
        all_data += x
    f.close()

    all_data = split(["Chapter"], all_data)

    newTxt = split(["."], sys.argv[1])
    newTxt = newTxt[0] + "_thai." + newTxt[1]
    f = open(newTxt, "w", encoding="utf8")
    for x in all_data:
        if len(x) > 6:
            x = "Chapter" + x
            #print(x)
            #print("-------------- " + str(len(x)) + "-------------- ")
            f.writelines(x)

            translated = GoogleTranslator(source='en', target='th').translate(x)
            print(translated)
            f.writelines(translated)

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

if __name__ == '__main__':
    main()
