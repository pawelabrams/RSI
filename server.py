#!/usr/bin/env python2
#  coding=utf-8
import time
import Pyro4 as pyro
import sys
from fractions import gcd
from functools import reduce
from __future__ import print_function

class DistributedGCD(Object):
    def __init__(self):
        self.ls = []
		self.ret = 1
	def setls(self, ls):
		self.ls = ls
	def dgcd(self):
		self.ret = reduce(lambda x, y: gcd(x,y), ls)
	def getret(self):
		return self.ret

if __name__ == '__main__':
    # pyro.config.SERIALIZER = "pickle"
    port_id = int(sys.argv[2])
    dg = DistributedGCD()
    print('DGCD started at port ' + str(port_id) + '!')
    pyro.Daemon.serveSimple( { dg: "dg" }, host = sys.argv[1], port = port_id, ns = False )
    while 1:
        time.sleep(0.1)
