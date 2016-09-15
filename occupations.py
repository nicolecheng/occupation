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

def readCSV(x):
    d = {}
    f = open(x)
    f.readline()
    m = f.readline()
    while m!='':
        if m[0]=='"':
            m = m[1:]
            n = m.index(m,'"') # finds index of second "
        else:
            n = m.index(m,',')
        d.addKey(m[0:n])
        d.addValue(m[n+1])
        m = f.readline()
    print d

readCSV("occupations.csv")


# string.index(s, sub[, start[, end]])
