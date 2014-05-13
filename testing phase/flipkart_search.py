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

def make_search_files(x):
    flipkart(x)
    amazon(x)
    amazon_india(x)

make_search_files("nokia lumia 520")
