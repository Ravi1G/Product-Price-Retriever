import os
import urllib
import urllib2
import webbrowser
from bs4 import BeautifulSoup

f=open('ebay_results.txt','r')
x=f.read()
soup=BeautifulSoup(x)
LMT=10
cnt=0
arr=[]
p1=[]
p2=[]
for x in soup.find_all('div','ittl'):
    print x
    b=x.get_text()
    if b:
        p1.append(b)
        cnt+=1
        if cnt>=LMT:
            break
        
cnt=0
for x in soup.find_all('div','g-b','price'):
    print x
    b=x.get_text()
    if b:
        c=""
        d=0
        r=0
        for i in range(len(b)):
            if b[i]>='0' and b[i]<='9':
                r=1
            if r==1 and (b[i]==' ' or b[i]=='\n'):
                break
            c+=b[i]
        p2.append(c)
        cnt+=1
        if cnt>=LMT:
            break
#print p1
#print p2
print len(p1)
print len(p2)

with open("ebay_scraped_results.txt","w") as f1:
    if len(p1)==0 or len(p2)==0:
        f1.write("No Search results found")
    else:
        if(len(p2)<LMT):
            LMT=len(p2)
        for m in range(LMT):
            arr.append("Product Name: "+p1[m]+"\nPrices\n: "+p2[m]+"\n\n")
            print arr[m]
            f1.write(arr[m])
