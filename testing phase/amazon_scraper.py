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
for x in soup.find_all('div','newPrice'):
    b=x.get_text()
    if b:
        c=""
        d=""
        r=0
        for i in range(len(b)):
            if b[i]=='$':
                r+=1
            if b[i]<='z' and b[i]>=' ':
                if r<2:
                    c+=b[i]
                else:
                    d+=b[i]
        if r==2:
            p2.append(d)
        else:
            p2.append(c)
        cnt+=1
        if cnt>=10:
            break
print p1
print p2
print len(p1)
print len(p2)

with open("amazon_scraped_results.txt","w") as f1:
    if(len(p1)==0 or len(p2)==0):
        f1.write("No Search results found")
    else:
        if len(p2)<LMT:
            LMT=len(p2)
        for m in range(LMT):
            arr.append("Product Name: "+p1[m]+"\n Prices \n: "+p2[m]+"\n\n")
            print arr[m]
            f1.write(arr[m])
