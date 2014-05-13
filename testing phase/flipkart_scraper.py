import os
import urllib
import urllib2
import webbrowser
from bs4 import BeautifulSoup
#from lxml import html

f=open('flipkart_results.txt','r')
#print f.read()
x=f.read()
soup=BeautifulSoup(x)
SEARCH_LIMIT=10
#print (soup.prettify())
cnt=0
arr=[]
for x in soup.find_all('div'):
    for a in x.find_all('div','pu-details lastUnit'):
        for b in a.find_all('div','pu-title fk-font-13'):
            for c in b.find_all('a','fk-display-block','prd-title'):
                d=c.get_text()
                p1= "Product Name:" + d
        if d:
            for b1 in a.find_all('div','pu-rating'):
                for c1 in b1.find_all('div'):
                    d1=c1.get('title')
                    if d1:
                        p2="Rating: " + d1
        if d:
            for b2 in a.find_all('div','pu-price'):
            #print "Price: " + b2.get_text()
                for c2 in b2.find_all('div','pu-border-top'):
                    for d2 in c2.find_all('div','pu-final'):
                        for e2 in d2.find_all('span'):
                            if e2:
                                p3= "Price: " + e2.get_text()
                                arr.append(p1+p2+"\n"+p3+"\n\n")
        cnt+=1
        if cnt>=10:
            break;

with open("flipkart_scraped_results.txt","w") as f1:
    if cnt==0:
        f1.write("No search Results Found")
    for m in range(SEARCH_LIMIT):
        print arr[m]
        f1.write(arr[m])
