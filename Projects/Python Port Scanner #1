Code:
#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #translate hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("Syntax: python3 scanner.py <ip>")

#Add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(dt.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print(f"Port {port} is open.")
		s.close()

except KeyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()

except socket.error:
	print("Could not connect to the server.")
	sys.exit()




Result:
                                                                                                                                                                              
┌──(kali㉿kali)-[~/python]
└─$ python3 scanner.py 192.168.1.1  
--------------------------------------------------
Scanning target 192.168.1.1
Time started: 2024-09-08 06:51:58.732208
--------------------------------------------------
Port 53 is open.
Port 80 is open.
                                                                                                                                                                              
┌──(kali㉿kali)-[~/python]
└─$ mousepad scanner.py    
