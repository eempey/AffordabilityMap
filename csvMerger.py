# -*- coding: utf-8 -*-
import csv
with open('shelter-by-tract.csv', 'rb') as f:
    with open('2006-census.csv', 'rb') as g:
        reader2011 = csv.reader(f)
        reader2006 = csv.reader(g)
        for row2011 in reader2011:
            print(row2011[0] + " " + reader2006[0][0])

