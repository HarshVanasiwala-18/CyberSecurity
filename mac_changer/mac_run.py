#!/usr/bin/env python

import mac_changer

options = mac_changer.get_arguments()

current_mac = mac_changer.get_current_mac(options.interface)
print("Current MAC : " + str(current_mac))

mac_changer.change_mac(options.interface, options.new_mac)

current_mac = mac_changer.get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to "+ current_mac)
else:
    print("[-] MAC address did not get changed.")