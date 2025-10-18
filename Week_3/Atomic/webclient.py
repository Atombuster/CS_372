import socket
import sys
import time


def system_seconds_since_1900():
    """
    The time server returns the number of seconds since 1900, but Unix
    systems return the number of seconds since 1970. This function
    computes the number of seconds since 1900 on the system.
    """

    # Number of seconds between 1900-01-01 and 1970-01-01
    seconds_delta = 2208988800

    seconds_since_unix_epoch = int(time.time())
    seconds_since_1900_epoch = seconds_since_unix_epoch + seconds_delta
    
    return seconds_since_1900_epoch

domain = "time.nist.gov"
port = 37 
#Make socket and connect to server
s = socket.socket()
server = (domain, port)
s.connect(server)
request = f"GET / HTTP/1.1\r\nHost: {domain}\r\nConnection: close\r\n\r\n"
s.sendall(request.encode('utf-8'))   



data = s.recv(4)
time.sleep(4)
s.close()

the_time = int.from_bytes(data, "big")
  
print("NIST time    : "+str(the_time))
print("System time: ",system_seconds_since_1900())
    
s.close()