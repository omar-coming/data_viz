import csv
import operator

sample=open('data.txt','r')

csv1 = csv.reader(sample,delimiter=',')

sort = sorted(csv1, key=operator.itemgetter(5))

for eachline in sort:
       print(eachline)
