# -*- coding: utf-8 -*-
hugehairypants = ['huge','hairy','pants']
smallsmoothskirt = ['small','smooth','skirt']

#for i in hugehairypants:
#    #print(i)
#    for j in smallsmoothskirt:
#        print(i +" " +j)

import csv
with open('shelter-by-tract.csv', 'rb') as f:
    with open('2006-census.csv', 'rb') as g:
        reader2011 = csv.reader(f)
        reader2006 = csv.reader(g)
        for row2011 in reader2011:
            print("2011: "+ row2011[0])            
            for row2006 in reader2006:                
                print("2006: " + row2006[0])

