import csv
import sys

try :
    fr = open("data.csv")
    fw = open("total_medals_country.csv", "w")
except:
    print("Couldn't open the file")

reader = csv.reader(fr)

counterlist = list()
for row in reader :
     #   print row
     if len(row) > 0 :
        counterlist.append(row[5])
    #for item in counterlist :
    #    print counterlist.count(item)

writer = csv.writer(fw)
data = ["MEDALS", "Count"]
writer.writerow(data)
for item in counterlist :
    rowdata = [item, counterlist.count(item)]
     #   print rowdata
    writer.writerow(rowdata)

fr.close();
fw.close();