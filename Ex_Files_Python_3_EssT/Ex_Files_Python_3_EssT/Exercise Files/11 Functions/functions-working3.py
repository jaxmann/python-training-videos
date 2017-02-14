#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    for n in testfunc():
        print(n)

def testfunc():
    return range(25)

if __name__ == "__main__": main()
