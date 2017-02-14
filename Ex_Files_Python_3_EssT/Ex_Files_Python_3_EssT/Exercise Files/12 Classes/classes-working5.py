#!/usr/bin/python3
# classes.py by Bill Weinman [http://bw.org/]
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Group, LLC

class Duck:
    def quack(self):
        print('Quaaack!')

    def walk(self):
        print('Walks like a duck.')

    def bark(self):
        print('the duck cannot bark')

    def fur(self):
        print('the duck has featherse')

class Dog:
    def bark(self):
        print('Woof')

    def fur(self):
        print('the dog has brown and white fur')

    def walk(self):
        print('the dog walks')

    def quack(self):
        print('the dog cannot quack')

def main():
    donald = Duck()
    fido = Dog()
    in_the_forest(donald)
    in_the_pond(fido)

def in_the_forest(dog):
    dog.bark()
    dog.fur()

def in_the_pond(duck):
    duck.quack()
    duck.walk()

if __name__ == "__main__": main()
