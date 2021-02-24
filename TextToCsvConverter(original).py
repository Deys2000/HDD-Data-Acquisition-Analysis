# Text to CSV

import csv

f = open("commandlineProjectDuplicate.txt")

x = f.readlines()
s = []
directoryLine = ""
count = -2

for i in x:
    if (i.find("<DIR>")<0 and i.find("File(s)")<0):
        if( i.find(" Directory of ")>-1):
            i = i.replace(" Directory of ","")
            directoryLine = i+" "
        else:
            i = i.lstrip()
            if ( i != ""):
                count = count + 1
                j = str(count) + "," + str(directoryLine.count("\\"))+ "," +directoryLine
                k = i[0:11] + "," + i[11:23] + ","+ i[23:39] + ","+i[39:]
                j = j.strip()
                k = k.strip()
                l = "\n"+ j + "," + k
                m = l.replace(" ","")
                s.append(m)

csvEx = csv.writer(open("commandlineProjectDuplicateConverted","w"))
csvEx.writerow(s)

f.close()

