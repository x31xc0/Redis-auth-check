import sys
import time
import telnetlib
import socket
import signal

class colors:
    SUCCESS = '\033[92m'
    ERROR = '\033[91m'
    DEFAULT = '\033[0m'

#Define host: TODO: Read from file
host = "127.0.0.1"
redisPort = 6379

def signal_handler(signal, frame):
        print "[-] SIGINT captured. Closing"
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def main():
    #Test connection
    try:
        telnet = telnetlib.Telnet(host, redisPort)
    except socket.error:
        print colors.ERROR + "Error connecting to "+host+" on port " + str(redisPort) + colors.DEFAULT
        exit(1)

    print colors.SUCCESS + "Sucessfully connected to "+host+" on port " + str(redisPort) + colors.DEFAULT

    telnet.write("echo success\r\n")
    response = telnet.read_all()

    print response
    pass



if __name__ == '__main__':
    sys.exit(main())
