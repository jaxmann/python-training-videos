#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(42, 61)

def testfunc(number, another = None, onemore = 75):
    if another is None:
            another = 112
    print('this is a test function', number, another, onemore)

if __name__ == "__main__": main()
