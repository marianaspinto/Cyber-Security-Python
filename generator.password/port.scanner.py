import nmap
import os

os.environ["PATH"] += r";C:\Program Files (x86)\Nmap"

# this object will be responsible for executing Nmap commands and processing the scan reuslts
nm = nmap.PortScanner()

target = "45.33.32.156"
options = "-sV -sC -oN scan_results.txt"
# -sV: detects the version of services running on open ports
# -sC: executes default Nmap scripts to gather more information

# performs the network scan
nm.scan(target, arguments=options)

# print information about each host an port discovered after the scan
for host in nm.all_hosts():
    print("Host: %s (%s)" % (host, nm[host].hostname()))
    print("State: %s" % nm[host].state())
    for protocol in nm[host].all_protocols():
        print("Protocol: %s" % protocol)
        port_info = nm[host][protocol]
        for port, state in port_info.items():
            print("Port: %s\tState: %s" % (port, state))