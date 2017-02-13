#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
    #different from doing a = b and b = a + b on two lines - in this case both oeprations happen at the same time
print("Done.")
