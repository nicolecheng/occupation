#!/usr/bin/python

'''Attached to the post (and placed in the workshop) is a .csv file that contains information about occupations in the United States (Courtesy of Mr. Brooks). Each line looks something like this:
    Legal,0.8
    "Education, training and library",6.1
The first item is the name of the occupation and the second is the percentage that occupation makes up of the U.S. workforce. Note that when the occupation has a comma in it, it is surrounded by quotation marks.

Your job (in pairs):
Read in the file and build an appropriate dictionary from it. Make sure the percentages are stored as numbers.
Create a function that returns a randomly selected occupation where the results are weighted by the percentage given. For example, there should be a 6.1% chance that "Education, training an library" is returned.
File this under occupation'''

import csv
import random

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
def picker(dict):
    percentage = random.random() * 99.8
    counter = 0
    for item in dict:
        if percentage > dict[item] + counter:
            counter += dict[item]
        else:
            return item
def occupation():
    dict = convertDict("occupations.csv")
    return picker(dict)
print occupation()


# string.index(s, sub[, start[, end]])
