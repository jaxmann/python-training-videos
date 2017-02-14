#!/usr/bin/python3
# functions.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

def main():
    testfunc(1, 2, 3, 4, 5, one = 1, two = 2, four = 42)

def testfunc(this, that, other, *args, **kwargs):
    for k in kwargs:
        print(k, kwargs[k])


if __name__ == "__main__": main()
