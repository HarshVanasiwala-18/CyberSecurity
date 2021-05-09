#!/user/bin/env python

import sniffer
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest = "interface", help = "Network Interface")
    options = parser.parse_args()
    
    if not options.interface:
        parser.error("[-] Please specify Network Interface, use --help for more info.")
    return options.interface

interface = get_arguments()

sniffer.sniff(interface)