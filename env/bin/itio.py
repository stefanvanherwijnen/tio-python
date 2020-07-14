#!/home/stefan/Projects/Heijmans/tio-python/env/bin/python
"""
itio: Interactive Twinleaf I/O 
License: MIT
Author: Thomas Kornack <kornack@twinleaf.com>
"""

import tldevicesync
import argparse

parser = argparse.ArgumentParser(prog='itio', 
                                 description='Interactive Twinleaf I/O.')

parser.add_argument("url", 
                    nargs='?', 
                    default='tcp://localhost/',
                    help='URL: tcp://localhost')
parser.add_argument("--rpc", 
                    action='append', 
                    default=[],
                    type=lambda kv: kv.split(":"), 
                    help='Commands to be sent on start; rpc:type:val')
parser.add_argument('-v', 
                    action="store_true",
                    default=False,
                    help='Verbose output for debugging')
parser.add_argument('-r', 
                    action="store_false",
                    default=True,
                    help='Ignore and rebuild rpc/stream cache')
args = parser.parse_args()

device = tldevicesync.DeviceSync(url=args.url, verbose=args.v, rpcs=args.rpc, stateCache=args.r)
device._interact()
