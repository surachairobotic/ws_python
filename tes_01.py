#!/usr/bin/env python3

def main():
    print( sum([x+35 if x>60 else x+25 for x in [35,78,56,92,45,56,98,250,60,300]]) )

if __name__ == "__main__":
    main()
