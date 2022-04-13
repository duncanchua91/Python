#!/usr/bin/python3
#Please install required software before executing script!
# su - root
# pip3 install python-nmap

import nmap #import nmap module

NmapScanner = nmap.PortScanner() #nmap port scanner class which allows you to use nmap from python

print("Welcome, this is simple nmap automation tool")
print("<--------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ") #create variable call ip_addr to equal the input
print("The IP you entered is: ", ip_addr) #display what IP address the user has entered
type(ip_addr) #sanitize input to make sure no other texts are entered (e.g. no string values)

#create a variable to capture user input for options 1, 2 or 3
resp = input("""\nPlease enter the type of scan you want to run
		1)SYN ACK Scan
		2)UDP Scan
		3)Comprehensive Scan \n""")
print("You have selected option: ", resp)

#option 1 = SYN ACK Scan
if resp == '1':
	print("Nmap Version: ", NmapScanner.nmap_version()) #print out Nmap version
	NmapScanner.scan(ip_addr, '1-1024', '-v -sS') #Nmap arguments required (IP address to scan, no. of ports to scan, and type of scan)
	print(NmapScanner.scaninfo()) #print out scan info e.g. TCP, services, and method
	print("IP Status: ", NmapScanner[ip_addr].state()) #print IP address status e.g. if it is active/reachable or inactive/unreachable
	print(NmapScanner[ip_addr].all_protocols()) #print the protocol we are scanning for 
	print("Open Ports: ", NmapScanner[ip_addr]['tcp'].keys()) #print all open ports using key methods, which return all active ports within range

#Option 2 = UDP Scan
elif resp == '2':
	print("Nmap Version: ", NmapScanner.nmap_version()) #print out Nmap version
	NmapScanner.scan(ip_addr, '1-1024', '-v -sU') #Nmap arguments required (IP address to scan, no. of ports to scan, and type of scan)
	print(NmapScanner.scaninfo()) #print out scan info e.g. TCP, services, and method
	print("IP Status: ", NmapScanner[ip_addr].state()) #print IP address status e.g. if it is active/reachable or inactive/unreachable
	print(NmapScanner[ip_addr].all_protocols()) #print the protocol we are scanning for
	print("Open Ports: ", NmapScanner[ip_addr]['udp'].keys()) #print all open ports using key methods, which return all active ports within range

#Option 3 = Comprehensive Scan
elif resp == '3':
	print("Nmap Version: ", NmapScanner.nmap_version()) #print out Nmap version
	NmapScanner.scan(ip_addr, '1-1024', '-v -sS -sV -sC -A -O') #Nmap arguments required (IP address to scan, no. of ports to scan, and type of scan)
	print(NmapScanner.scaninfo()) #print out scan info e.g. TCP, services, and method
	print("IP Status: ", NmapScanner[ip_addr].state()) #print IP address status e.g. if it is active/reachable or inactive/unreachable
	print(NmapScanner[ip_addr].all_protocols()) #print the protocol we are scanning for
	print("Open Ports: ", NmapScanner[ip_addr]['tcp'].keys()) #print all open ports using key methods, which return all active ports within range

#Option 4 = validation e.g. if not option 1, 2 or 3, then prompt user to enter valid option
else:
	print("Please enter a valid option")

	
	
	
	
	
	
