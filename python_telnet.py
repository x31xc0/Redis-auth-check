# Author: x31xc0
# Date: 03/03/2016
# Name: Redis AUTH check
import sys
import time
import telnetlib
import socket
import signal
from subprocess import call, check_output

# Set terminal colors
class colors:
    SUCCESS = '\033[92m'
    ERROR = '\033[91m'
    INFO = '\033[93m'
    DEFAULT = '\033[0m'

# TODO: Fill out generic connection class
class telnet:
    telnetCon = ''

#Define host: TODO: Read from file
host = "127.0.0.1"
redisPort = 6379
timeout = 60 #This may need to be adjusted

def signal_handler(signal, frame):
        print "[-] SIGINT captured. Closing"
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main():
    #Test connection
    if(CheckHostTelnetConnnection()):
        GenerateRsaKey()
    pass

def CheckHostTelnetConnnection():
    try:
        telnet.telnetCon = telnetlib.Telnet(host, redisPort, timeout = timeout)
    except socket.error:
        print colors.ERROR + "[-] Error connecting to "+host+" on port " + str(redisPort) + colors.DEFAULT
        exit(1)
    print colors.SUCCESS + "\n[+] Sucessfully connected to "+host+" on port " + str(redisPort) + colors.DEFAULT
    print colors.INFO + "\nTesting for AUTH\n" + colors.DEFAULT

    telnet.telnetCon.write("echo noauth\r\n")
    time.sleep(1) #Temp solution?
    response = (telnet.telnetCon.read_eager().decode('ascii'))

    if "noauth" in response:
        print colors.SUCCESS + "[+] No AUTH set" + colors.DEFAULT
        return 1 # Success
    else:
        #TODO: Add more refined checking for if(AUTH)
        print + color.ERROR + "[-] AUTH set" + colors.DEFAULT

    pass

def GenerateRsaKey():
    #TODO: Add options for custom passphrase, note and save location
    user = check_output(["whoami"]).strip()
    print colors.INFO + "\nGenerating RSA key\n" + colors.DEFAULT
    if(call(["ssh-keygen", "-q" ,"-t", "rsa","-f", "/"+user+"/.ssh/id_rsa", "-C", "'redis'" ,"-N", "x31xc0"]) == 0):
        print colors.SUCCESS + "\n[+] Successfully generated RSA key" + colors.DEFAULT


if __name__ == '__main__':
    sys.exit(main())
