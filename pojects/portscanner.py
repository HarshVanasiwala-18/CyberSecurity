import nmap

nmScan = nmap.PortScanner()

ipAdd = ("Enter Ip Address : ")

for host in nmScan.all_hosts():
     print('Host : %s (%s)' % (host, nmScan[host].hostname()))
     print('State : %s' % nmScan[host].state())
     for protocol in nmScan[host].all_protocols():
         print('----------')
         print('Protocol : %s' % protocol)
 
         lport = nmScan[host][proto].keys()
         lport.sort()
         for port in lport:
             print ('port : %s\tstate : %s' % (port, nmScan[host][proto][port]['state'])
