from files import store
from files import fileappender
from datetime import datetime

""" 
while True:
    record=input()
    if(len(record)==0):
        break
    fileappender('x.txt',record)
     """

""" for x in store["peoplelist"]:
    fileappender('new.txt',x) """

datalist=store["linelist"]('sample.py')
fileappender('appender2.txt',"\n-----------{}------------\n".format(datetime.now()))
firstline=int(input('enter the beginning line no to read-->'))
lastline=int(input('enter the ending line no to read-->'))
sliced=datalist[firstline-1:lastline+1]
for x in sliced: 
    fileappender('appender2.txt',x)