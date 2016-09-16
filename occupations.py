#!/usr/bin/python

import random

def convertDict(x):
    d = {}
    f = open(x)
    f.readline()
    m = f.readline()
    while m!='':
        if m[0]=='"':
            m = m[1:]
            n = m.index('"')+1 # finds index of second "
            d[m[:n-1]] = float(m[n+1:])
        else:
            n = m.index(',')
            if(m[0:5]!='Total'):
                d[m[:n]] = float(m[n+1:]) # add the kv pair to d
        m = f.readline() # next line, por favor
    return d

def picker(dict):
    percentage = random.random() * 99.8
    counter = 0
    for item in dict:
        if percentage > dict[item] + counter:
            counter += dict[item]
        else:
            return item
        
def occupations():
    dict = convertDict("occupations.csv")
    return picker(dict)

print occupations()


'''
def convertDict(x):
    d = {}
    f = open(x)
    f.readline()
    m = f.readline()
    while m!='':
        if m[0]=='"':
            m = m[1:]
            indexOfEndQuote = m.find('"')
            currentJob = m[:indexOfEndQuote]
            d[currentJob] = float(m[indexOfEndQuote + 2:])
        else:
            if m[0:5] != 'Total':
                indexOfComma = m.find(',')
                currentJob = m[:indexOfComma]
                d[currentJob] = float(m[indexOfComma + 1:])
        m = f.readline()
    return d
'''
