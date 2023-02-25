# Kobe Luna
# StudentID: P21590963
# Problem 1

import random
import math

queue = "kobe luna"
MyList = ["Kobe Bryant", "Kobe, Japan", "Luna is moon in spanish", "Kobe was my favorite player", "Luna brothers"]

match = [0] * len(MyList)

def Frequency(term, mylist):
    fq = 0
    start = 0
    while True:
        start = mylist.find(term, start)
        if start >= 0:
            start += len(term)
            fq += 1
        else:
            return fq



fqterms = queue.split()

for i in range(len(MyList)):
    for j in range (len(fqterms)):
        fq = Frequency(fqterms[j].lower(), MyList[i].lower())
        if fq > 0:
            match[i]+= 1 + math.log(fq, 10)

def myFunc(n):
    return match[MyList_copy.index(n)] # n is the element in MyList

MyList_copy = MyList[:]
MyList = sorted(MyList, key = myFunc)
print(match)
print(MyList)

