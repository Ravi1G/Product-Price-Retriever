import os
import urllib
import urllib2
import webbrowser
from bs4 import BeautifulSoup
#from lxml import html

f=open('amazon_results.txt','r')
x=f.read()
soup=BeautifulSoup(x)
LMT=10
cnt=0
val=0
arr=[]
for val in range(1,LMT+1):
    v=""
    v+='result_'+str(val)
    print v
    for x in soup.findall('div',str(v)):
        for a in x.findall('a'):
            f=1
            for b in a.find_all('span','lrg bold'):
                c=b.get_text()
                if c:
                    p1="Product Name:"+c
                    print p1
            for b in a.find_all('span','med reg'):
                c=b.get_text()
                if c:
                    p2=c
                    print c
            for b in a.find_all('span','price bld'):
                c=b.get_text()
                if c:
                    if f==1:
                        p3="new: "+c
                        f=1-f
                    else:
                        p3="used: "+c
                    print p3
            arr.append(p1+"\n"+p2+"\n"++p3+"\n\n")
                
        

with open("amazon_scraped_results.txt","w") as f1:
    for m in range(SEARCH_LIMIT):
        print arr[m]
        f1.write(arr[m])
