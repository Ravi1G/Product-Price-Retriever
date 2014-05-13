import os
import urllib
import urllib2
import webbrowser
from bs4 import BeautifulSoup

def flipkart(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.flipkart.com/search"
    data=urllib.urlencode({'q':x1,'as':'off','as-show':'on','otracker':'start','as-pos':'1_q'})
    results=urllib2.urlopen(url,data)
    global flipkart1
    flipkart1=results.read()
    print "search results from flipkart saved..."

def amazon_india(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.amazon.in/s/ref=nb_sb_noss_2"
    data=urllib.urlencode({'url':'search-alias%3Daps','field-keywords':x1,'rh':'i%3Aaps%2Ck%3A'+x1})
    results=urllib2.urlopen(url,data)
    global amazon_india1
    amazon_india1=results.read()
    #with open("amazon_india_results.txt","w") as f:
    #    f.write(results.read())
    print "search results from amazon_india saved..."

def amazon(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.amazon.com/s/ref=nb_sb_noss_1"
    data=urllib.urlencode({'url':'search-alias%3Daps','field-keywords':x1,'rh':'i%3Aaps%2Ck%3A'+x1})
    results=urllib2.urlopen(url,data)
    global amazon1
    amazon1=results.read()
    #with open("amazon_results.txt","w") as f:
    #    f.write(results.read())
    print "search results from amazon saved..."

def yebhi(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='%20'
    x1="".join(s)
    url="http://www.yebhi.com/searchAll.aspx"
    data=urllib.urlencode({'q':x1})
    results=urllib2.urlopen(url,data)
    global yebhi1
    yebhi1=results.read()
    #with open("yebhi_results.txt","w") as f:
    #    f.write(results.read())
    print "search results from yebhi saved..."

def snapdeal(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.snapdeal.com/search"
    data=urllib.urlencode({'keyword':x1,'santizedKeyword':'','catId':'','categoryId':'0','suggested':'false','vertical':'','noOfResults':'20','clickSrc':'go_header','lastKeyword':'','prodCatId':'','changeBackToAll':'false','foundInAll':'false','categoryIdSearched':'','cityPageUrl':'','url':'','utmContent':'','catalogID':'','dealDetail':''})
    results=urllib2.urlopen(url,data)
    global snapdeal1
    snapdeal1=results.read()
    #with open("snapdeal_results.txt","w") as f:
    #    f.write(results.read())
    print "search results from snapdeal saved..."

def ebay(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.ebay.in/sch/i.html"
    data=urllib.urlencode({'_trksid':'p2050601.m570.l1311.R1.TR3.TRC0.A0.X'+x,'_nkw':x1,'_sacat':'0','_from':'R40'})
    results=urllib2.urlopen(url,data)
    global ebay1
    ebay1=results.read()
    #with open("ebay_results.txt","w") as f:
    #    f.write(results.read())
    print "search results from ebay saved..."

def junglee(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.junglee.com/mn/search/junglee/ref=nav_sb_noss"
    data=urllib.urlencode({'url':'search-alias%3Daps','field-keywords':x})
    results=urllib2.urlopen(url,data)
    global junglee1
    junglee1=results.read()
    #with open("junglee_results.txt","w") as f:
    #    f.write(results.read())
    print "search results from junglee saved..."


def make_search(x):
    print "Getting the search result from all the websites:"
    print "..."
    amazon(x)
    flipkart(x)
    amazon_india(x)
    snapdeal(x)
    ebay(x)
    junglee(x)
    #yebhi(x)

arrf=[]
arrs=[]
arra=[]
arri=[]
arrj=[]
arre=[]

def flipkart_scraper():
    soup=BeautifulSoup(flipkart1)
    cnt=0
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
                                    arrf.append(p1+p2+"\n"+p3+"\n\n")
            cnt+=1
            if cnt>=LMT:
                break
        if cnt>=LMT:
            break
    if cnt==0:
        arrf.append("No search Results Found")

def amazon_scraper():
    soup=BeautifulSoup(amazon1)
    cnt=0
    p1=[]
    p2=[]
    for x in soup.find_all('div','productTitle'):
        b=x.get_text()
        if b:
            p1.append(b)
            #print "Product Name:" + b
            cnt+=1
            if cnt>=LMT:
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
            if cnt>=LMT:
                break
    if(len(p1)==0 or len(p2)==0):
        arra.append("No Search results found")
    else:
        limt=LMT;
        if len(p2)<LMT:
            limt=len(p2)
        if len(p1)<limt:
            limt=len(p1)
        for m in range(limt):
            arra.append("Product Name: "+p1[m]+"\n Prices \n: "+p2[m]+"\n\n")

def amazon_india_scraper():
    soup=BeautifulSoup(amazon_india1)
    cnt=0
    p1=[]
    p2=[]
    for x in soup.find_all('div','productTitle'):
        b=x.get_text()
        if b:
            p1.append(b)
            #print "Product Name:" + b
            cnt+=1
            if cnt>=LMT:
                break
            
    cnt=0
    for x in soup.find_all('div','newPrice'):
        b=x.get_text()
        #print b
        if b:
            c=""
            d=""
            r=0
            for i in range(len(b)):
                if b[i]=='R':
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
            if cnt>=LMT:
                break
    if(len(p1)==0 or len(p2)==0):
        arri.append("No Search Results Found")
    else:
        limt=LMT;
        if len(p2)<LMT:
            limt=len(p2)
        if len(p1)<limt:
            limt=len(p1)
        for m in range(limt):
            arri.append("Product Name: "+p1[m]+"\nPrices\n: "+p2[m]+"\n\n")

def snapdeal_scraper():
    soup=BeautifulSoup(snapdeal1)
    cnt=0
    p1=[]
    p2=[]
    for x in soup.find_all('div','product_listing_heading fnt-tahoma'):
        b=x.get_text()
        if b:
            p1.append(b)
            cnt+=1
            if cnt>=LMT:
                break
    cnt=0
    for x in soup.find_all('div','product_price '):
        b=x.get_text()
        if b:
            c=""
            d=""
            r=0
            for i in range(len(b)):
                if b[i]=='R':
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
            if cnt>=LMT:
                break
    if(len(p1)==0 or len(p2)==0):
        arrs.append("No Search Results Found")
    else:
        limt=LMT;
        if len(p2)<LMT:
            limt=len(p2)
        if len(p1)<limt:
            limt=len(p1)
        for m in range(limt):
            arrs.append("Product Name: "+p1[m]+"\nPrices\n: "+p2[m]+"\n\n")

def junglee_scraper():
    soup=BeautifulSoup(junglee1)
    cnt=0
    p1=[]
    p2=[]
    for x in soup.find_all('a','title'):
        b=x.get_text()
        #print "b" + b
        if b:
            p1.append(b)
            cnt+=1
            if cnt>=LMT:
                break
    cnt=0
    for x in soup.find_all('span','price'):
        b=x.get_text()
        if b:
            c=""
            d=""
            r=0
            for i in range(len(b)):
                if b[i]=='R':
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
            if cnt>=LMT:
                break
    if(len(p1)==0 or len(p2)==0):
        arrj.append("No Search Results Found")
    else:
        limt=LMT;
        if len(p2)<LMT:
            limt=len(p2)
        if len(p1)<limt:
            limt=len(p1)
        for m in range(limt):
            arrj.append("Product Name: "+p1[m]+"\nPrices\n: Rs. "+p2[m]+"\n\n")

def ebay_scraper():
    soup=BeautifulSoup(ebay1)
    cnt=0
    p1=[]
    p2=[]
    for x in soup.find_all('div','ittl'):
        b=x.get_text()
        if b:
            p1.append(b)
            cnt+=1
            if cnt>=LMT:
                break 
    cnt=0
    for x in soup.find_all('div','g-b','price','b'):
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
    if(len(p1)==0 or len(p2)==0):
        arre.append("No Search Reply Found")
    else:
        limt=LMT;
        if len(p2)<LMT:
            limt=len(p2)
        if len(p1)<limt:
            limt=len(p1)
        for m in range(limt):
            arre.append("Product Name: "+p1[m]+"\nPrices\n: "+p2[m]+"\n\n")



def scrape_all():
    flipkart_scraper()
    amazon_scraper()
    amazon_india_scraper()
    snapdeal_scraper()
    junglee_scraper()
    ebay_scraper()

def print_all():
    with open("lotus.txt","w") as f1:
        st="Best "+str(LMT)+" matches available in the market:\n\n"
        f1.write(st)
        f1.write("-----------------------------------------------------------------------------------------")
        f1.write("\nFLIPKART RESULTS:\n")
        for i in arrf: f1.write(i)
        f1.write("-----------------------------------------------------------------------------------------")
        f1.write("\nAMAZON RESULTS:\n")
        for i in arra: f1.write(i)
        f1.write("-----------------------------------------------------------------------------------------")
        f1.write("\nAMAZON INDIA RESULTS:\n")
        for i in arri: f1.write(i)
        f1.write("-----------------------------------------------------------------------------------------")
        f1.write("\nSNAPDEAL RESULTS:\n")
        for i in arrs: f1.write(i)
        f1.write("-----------------------------------------------------------------------------------------")
        f1.write("\nJUNGLEE RESULTS:\n")
        for i in arrj: f1.write(i)
        f1.write("-----------------------------------------------------------------------------------------")
        f1.write("\nEBAY RESULTS:\n")
        for i in arre: f1.write(i)
        print "Check out the results in the file <lotus.txt>"
        

print "Enter the item, you wish to search..."
x=raw_input()
print "Enter the degree of search..."#number of search results from each site
LMT=int(raw_input())
make_search(x)
scrape_all()
print_all()
