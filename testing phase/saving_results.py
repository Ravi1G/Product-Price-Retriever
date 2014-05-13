import urllib
import urllib2
import webbrowser

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
    with open("flipkart_results.txt","w") as f:
        f.write(results.read())
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
    with open("amazon_india_results.txt","w") as f:
        f.write(results.read())
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
    with open("amazon_results.txt","w") as f:
        f.write(results.read())
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
    with open("yebhi_results.txt","w") as f:
        f.write(results.read())
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
    with open("snapdeal_results.txt","w") as f:
        f.write(results.read())
    print "search results from snapdeal saved..."

def ebay(x):
    y=len(x)
    s=list(x)
    for i in range(y):
        if s[i]==' ':
            s[i]='+'
    x1="".join(s)
    url="http://www.ebay.in/sch/i.html"
    data=urllib.urlencode({'_trksid':'p2050601.m570.l1311.R1.TR3.TRC0.A0.H0.X'+x1,'_nkw':x1,'_sacat':'0','_from':'R40'})
    results=urllib2.urlopen(url,data)
    with open("ebay_results.txt","w") as f:
        f.write(results.read())
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
    with open("junglee_results.txt","w") as f:
        f.write(results.read())
    print "search results from junglee saved..."


def make_search_files(x):
    print "Saving the result web pages for all the websites searches:"
    print "."
    print ".."
    print "..."
    flipkart(x)
    amazon(x)
    amazon_india(x)
    snapdeal(x)
    yebhi(x)
    ebay(x)
    junglee(x)

x=raw_input()
make_search_files(x)
