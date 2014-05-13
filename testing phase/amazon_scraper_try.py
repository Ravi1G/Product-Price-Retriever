import os
import urllib
import urllib2
import webbrowser
from bs4 import BeautifulSoup

f=open('amazon_results.txt','r')
x=f.read()
soup=BeautifulSoup(x)
LMT=10
cnt=0
arr=[]
p1=[]
p2=[]
for x in soup.find_all('div','productTitle'):
    b=x.get_text()
    if b:
        p1.append(b)
        #print "Product Name:" + b
        cnt+=1
        if cnt>=10:
            break
        
cnt=0
for x in soup.find_all('div','usedNewPrice'):
    b=x.get_text()
    if b:
        p2.append(b)
        #print "prices: " + b
        cnt+=1
        if cnt>=10:
            break
print p1
print p2
#print len(p1)
#print len(p2)

with open("amazon_scraped_results.txt","w") as f1:
    for m in range(LMT):
        arr.append("Product Name: "+p1[m]+"\nPrices\n: "+p2[m]+"\n\n")
        print arr[m]
        f1.write(arr[m])
