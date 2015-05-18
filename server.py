# coding=utf-8
import time
import Pyro4 as pyro
import sys
from fractions import gcd
from functools import reduce
from __future__ import print_function

class DistributedGCD(Object):
	def dgcd(ls):
		return reduce(lambda x, y: gcd(x,y), ls)

if __name__ == '__main__':
    # pyro.config.SERIALIZER = "pickle"
    port_id = int(sys.argv[2])
    dg = DistributedGCD()
    print('DGCD started at port ' + str(port_id) + '!')
    pyro.Daemon.serveSimple( { dg: "dg" }, host = sys.argv[1], port = port_id, ns = False )
    while 1:
        time.sleep(0.1)
