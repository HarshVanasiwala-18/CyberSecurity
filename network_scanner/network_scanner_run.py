#!/user/bin/env python

import network_scanner as netscan

options = netscan.get_arguments()
scan_result = netscan.scan(options.target)
netscan.print_result(scan_result)