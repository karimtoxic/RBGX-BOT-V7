#################################

import socket
import select
import requests
import threading
import re
import time
import struct
import struct
import urllib3
import random

#################################

RbGx = False
back = False
enc_client_id = None
inviteD = False
inviteD = False
back = False
invit_spam = False

#################################

SOCKS_VERSION = 5

#################################


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


#################################


def generate_random_color():
	color_list = [
    "[00FF00][b][c]",
    "[FFDD00][b][c]",
    "[3813F3][b][c]",
    "[FF0000][b][c]",
    "[0000FF][b][c]",
    "[FFA500][b][c]",
    "[DF07F8][b][c]",
    "[11EAFD][b][c]",
    "[DCE775][b][c]",
    "[A8E6CF][b][c]",
    "[7CB342][b][c]",
    "[FF0000][b][c]",
    "[FFB300][b][c]",
    "[90EE90][b][c]"
]
	random_color = random.choice(color_list)
	return  random_color
	
	
	
#################################


	
yout1 = b"\x06\x00\x00\x00{\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*o\x08\x81\x80\x83\xb6\x01\x1a)[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf\xe3\x85\xa4\xd8\xa7\xd9\x84\xd8\xa8\xd9\x87\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xdc)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\tAO'-'TEAM\xf0\x01\x01\xf8\x01\xdc\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02F"
yout2 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xd6\xd1\xb9(\x1a![18ffff]\xef\xbc\xa8\xef\xbc\xac\xe3\x85\xa4Hassone.[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xcf\x1e\xd8\x01\xcc\xd6\xd0\xad\x03\xe0\x01\xed\xdc\x8d\xae\x03\xea\x01\x1d\xef\xbc\xb4\xef\xbc\xa8\xef\xbc\xa5\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xac\xef\xbc\xac\xe0\xbf\x90\xc2\xb9\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout3 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xe9\xa7\xe9\x1b\x1a [18ffff]DS\xe3\x85\xa4WAJIHANO\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xca2\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x10.DICTATORS\xe3\x85\xa4\xe2\x88\x9a\xf0\x01\x01\xf8\x01\xc4\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout4 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*n\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout5 = b"\x06\x00\x00\x00\x84\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*x\x08\xb6\xc0\xf1\xcc\x01\x1a'[18ffff]\xd9\x85\xd9\x84\xd9\x83\xd8\xa9*\xd9\x84\xd9\x85\xd8\xb9\xd9\x88\xd9\x82\xd9\x8a\xd9\x86[18ffff]2\x02ME@G\xb0\x01\x05\xb8\x01\x82\x0b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x15\xe9\xbf\x84\xef\xbc\xac\xef\xbc\xaf\xef\xbc\xb2\xef\xbc\xa4\xef\xbc\xb3\xe9\xbf\x84\xf0\x01\x01\xf8\x01>\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x05\xd8\x02\x0e"
yout6 = b'\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xeb\x98\x88\x8e\x01\x1a"[18ffff]OP\xe3\x85\xa4BNL\xe3\x85\xa4\xe2\x9a\xa1\xe3\x85\xa4*[18ffff]2\x02ME@R\xb0\x01\x10\xb8\x01\xce\x16\xd8\x01\x84\xf0\xd2\xad\x03\xe0\x01\xa8\xdb\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x8f\xe1\xb4\xa0\xe1\xb4\x87\xca\x80\xe3\x85\xa4\xe1\xb4\x98\xe1\xb4\x8f\xe1\xb4\xa1\xe1\xb4\x87\xca\x80\xe2\x9a\xa1\xf0\x01\x01\xf8\x01A\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01\xe0\x02\xf3\x94\xf6\xb1\x03'
yout7 = b"\x06\x00\x00\x00\x8e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x81\x01\x08\xb0\xa4\xdb\x80\x01\x1a'[18ffff]\xd9\x85\xd9\x83\xd8\xa7\xd9\x81\xd8\xad\xd8\xa9.\xe2\x84\x93\xca\x99\xe3\x80\xb5..[18ffff]2\x02ME@T\xb0\x01\x13\xb8\x01\xfc$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x1d\xef\xbc\xad\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa1\xe3\x85\xa4\xe2\x8e\xb0\xe2\x84\x93\xca\x99\xe2\x8e\xb1\xf0\x01\x01\xf8\x01\xdb\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0f\xd8\x02>"
yout8 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xfd\x8a\xde\xb4\x02\x1a\x1f[18ffff]ITZ\xe4\xb8\xb6MOHA\xe3\x85\xa42M[18ffff]2\x02ME@C\xb0\x01\n\xb8\x01\xdf\x0f\xd8\x01\xac\xd8\xd0\xad\x03\xe0\x01\xf2\xdc\x8d\xae\x03\xea\x01\x15\xe3\x80\x9dITZ\xe3\x80\x9e\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf8\x01\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x026'
yout9 = b'\x06\x00\x00\x00w\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*k\x08\xc6\x99\xddp\x1a\x1b[18ffff]HEROSHIIMA1[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa8\xef\xbc\xa5\xef\xbc\xb2\xef\xbc\xaf\xef\xbc\xb3\xef\xbc\xa8\xef\xbc\xa9\xef\xbc\xad\xef\xbc\xa1\xef\xa3\xbf\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout10 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout11 = b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout12 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout14 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout15 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\x90\xf6\x87\x15\x1a"[18ffff]V4\xe3\x85\xa4RIO\xe3\x85\xa46%\xe3\x85\xa4zt[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\x95&\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x0e\xe1\xb4\xa0\xe1\xb4\x80\xe1\xb4\x8d\xe1\xb4\x8f\xd1\x95\xf0\x01\x01\xf8\x01\xe2\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02^\xe0\x02\x85\xff\xf5\xb1\x03'
yout16 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout17 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout18 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout19 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout20 = b'\x06\x00\x00\x00p\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*d\x08\xde\x91\xb7Q\x1a\x1c[18ffff]SH\xe3\x85\xa4SHIMA|M[18ffff]2\x02ME@R\xb0\x01\x14\xb8\x01\xe7C\xd8\x01\xdd\xd6\xd0\xad\x03\xe0\x01\xca\xdb\x8d\xae\x03\xea\x01\tSH\xe3\x85\xa4Team\xf8\x014\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x11\xd8\x02G\xe0\x02\x89\xa0\xf8\xb1\x03'
yout21= b'\x06\x00\x00\x00h\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\\\x08\xa1\x9f\xb3\xf4\x01\x1a\x1b[18ffff]2JZ\xe3\x85\xa4POWER[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xa5(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xec\xdb\x8d\xae\x03\xf0\x01\x01\xf8\x01\x9a\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02.\xe0\x02\xb2\xe9\xf7\xb1\x03'
yout22 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\xaa\xe5\xa4\xe3\x01\x1a-[18ffff]\xe3\x85\xa4\xd8\xb4\xd9\x83\xd8\xa7\xd9\x8e\xd9\x83\xd9\x80\xd9\x8a\xe3\x80\x8e\xe2\x85\xb5\xe1\xb4\x98\xe3\x80\x8f[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\xf2*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xaf\xdb\x8d\xae\x03\xea\x01\x15\xe2\x80\xa2\xe3\x85\xa4\xe2\x93\x8b\xe2\x92\xbe\xe2\x93\x85\xe3\x85\xa4\xe2\x80\xa2\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02e\xe0\x02\xa0\xf1\xf7\xb1\x03'
yout23 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xfd\x8b\xf4\xfa\x01\x1a$[18ffff]"\xd8\xaf\xd8\xb1\xd8\xa7\xd8\xba\xd9\x88\xd9\x86\xd9\x80\xd9\x88\xd9\x81"[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xec \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe1\xb4\x98\xe1\xb4\x84\xe1\xb5\x80\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\xb0\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x04\xd8\x02\t\xe0\x02\xf2\x94\xf6\xb1\x03'
yout24 = b'\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xaa\x84\xc1r\x1a\x1f[18ffff]SA777RAWI\xe3\x85\xa4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xc8\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x0cSA7RAWI\xe3\x85\xa4TM\xf0\x01\x01\xf8\x01\xfe\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\t\xd8\x02 '
yout25 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xe7\xbf\xb6\x8f\x01\x1a\x1c[18ffff]SVG.NINJA\xe2\xbc\xbd[18ffff]2\x02ME@I\xb0\x01\x13\xb8\x01\x94\x1b\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x85\xdb\x8d\xae\x03\xea\x01\x15\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4\xe3\x85\xa4???\xe3\x85\xa4\xe3\x85\xa4\xf0\x01\x01\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02?'
yout26 = b"\x06\x00\x00\x00\x9d\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x90\x01\x08\xa8\xe8\x91\xd7\x01\x1a.[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe4\xba\x97\xef\xbc\xb9\xef\xbc\xb4\xe3\x85\xa4[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\x97'\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1e\xef\xbc\xa1\xef\xbc\xac\xef\xbc\x93\xef\xbc\xab\xef\xbc\xa5\xef\xbc\xa4\xe2\x80\xa2\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93\xf0\x01\x01\xf8\x01\xab\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x10\xd8\x02@\xe0\x02\xe9\x80\xf8\xb1\x03"
yout27 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9b\x94\xaa\r\x1a\x1c[18ffff]FARAMAWY_1M.[18ffff]2\x02ME@I\xb0\x01\x01\xb8\x01\xe8\x07\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01X\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout28 = b"\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xaa\xdd\xf1'\x1a\x1d[18ffff]BM\xe3\x85\xa4ABDOU_YT[18ffff]2\x02ME@G\xb0\x01\x13\xb8\x01\xd4$\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1d\xe2\x80\xa2\xc9\xae\xe1\xb4\x87\xca\x9f\xca\x9f\xe1\xb4\x80\xca\x8d\xe1\xb4\x80\xd2\x93\xc9\xaa\xe1\xb4\x80\xc2\xb0\xf0\x01\x01\xf8\x01\x8e\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x07\xd8\x02\x16"
yout29 = b'\x06\x00\x00\x00r\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*f\x08\x9a\xd6\xdcL\x1a-[18ffff]\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xe3\x85\xa4\xef\xbc\xa8\xef\xbc\xa1\xef\xbc\xa6\xef\xbc\xa9\xef\xbc\xa4\xef\xbc\xa9[18ffff]2\x02ME@H\xb0\x01\x01\xb8\x01\xe8\x07\xea\x01\x15\xe1\xb4\x8d\xcd\xa1\xcd\x9co\xc9\xb4\xef\xbd\x93\xe1\xb4\x9b\xe1\xb4\x87\xca\x80\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout30 = b'\x06\x00\x00\x00v\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*j\x08\xb6\x92\xa9\xc8\x01\x1a [18ffff]\xef\xbc\xaa\xef\xbc\xad\xef\xbc\xb2\xe3\x85\xa4200K[18ffff]2\x02ME@R\xb0\x01\x13\xb8\x01\xc3(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\n3KASH-TEAM\xf8\x012\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x06\xd8\x02\x13\xe0\x02\x89\xa0\xf8\xb1\x03'
yout31 = b"\x06\x00\x00\x00\x92\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x85\x01\x08\xa2\xd3\xf4\x81\x07\x1a'[18ffff]\xd8\xb3\xd9\x80\xd9\x86\xd9\x80\xd8\xaf\xd8\xb1\xd9\x8a\xd9\x84\xd8\xa71M\xe3\x85\xa4[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xc1 \xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xad\xef\xbc\xa6\xef\xbc\x95\xef\xbc\xb2\xef\xbc\xa8\xe3\x85\xa4\xe1\xb4\xa0\xc9\xaa\xe1\xb4\x98\xf0\x01\x01\xf8\x01\x8c\x01\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0e\xd8\x024\xe0\x02\x87\xff\xf5\xb1\x03"
yout32 = b'\x06\x00\x00\x00|\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*p\x08\xe0\xe1\xdeu\x1a\x1a[18ffff]P1\xe3\x85\xa4Fahad[18ffff]2\x02ME@N\xb0\x01\x13\xb8\x01\xd0&\xd8\x01\xea\xd6\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1a\xe3\x85\xa4\xef\xbc\xb0\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xa5\xef\xbc\xae\xef\xbc\xa9\xef\xbc\xb8\xc2\xb9\xf0\x01\x01\xf8\x01\x9e\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02*'
yout33 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\xc5\xcf\x94\x8b\x02\x1a\x18[18ffff]@EL9YSAR[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\x86+\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\x89\xae\x8f\xae\x03\xea\x01\x1d-\xc9\xaa\xe1\xb4\x8d\xe1\xb4\x8d\xe1\xb4\x8f\xca\x80\xe1\xb4\x9b\xe1\xb4\x80\xca\x9fs\xe2\xac\x86\xef\xb8\x8f\xf8\x01j\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xe2\x02\xe0\x02\x9f\xf1\xf7\xb1\x03'
yout34 = b'\x06\x00\x00\x00x\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*l\x08\xa9\x81\xe6^\x1a\x1e[18ffff]STRONG\xe3\x85\xa4CRONA[18ffff]2\x02ME@J\xb0\x01\x13\xb8\x01\xd8$\xd8\x01\xd8\xd6\xd0\xad\x03\xe0\x01\x92\xdb\x8d\xae\x03\xea\x01\x12\xe2\x80\xa2\xe3\x85\xa4STRONG\xe3\x85\xa4\xe2\x80\xa2\xf0\x01\x01\xf8\x01q\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\xbc\x01'
yout35 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xeb\x8d\x97\xec\x01\x1a&[18ffff]\xd8\xb9\xd9\x80\xd9\x85\xd9\x80\xd8\xaf\xd9\x86\xd9\x8a\xd9\x80\xd8\xaa\xd9\x80\xd9\x88[18ffff]2\x02ME@F\xb0\x01\x13\xb8\x01\xd3\x1a\xd8\x01\xaf\xd7\xd0\xad\x03\xe0\x01\xf4\xdc\x8d\xae\x03\xea\x01\rOSIRIS\xe3\x85\xa4MASR\xf8\x01o\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02\\\xe0\x02\xf4\x94\xf6\xb1\x03'
yout36 = b'\x06\x00\x00\x00\x7f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*s\x08\xb4\xff\xa3\xef\x01\x1a\x1c[18ffff]ZAIN_YT_500K[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xa3#\xd8\x01\xa2\xd7\xd0\xad\x03\xe0\x01\xbb\xdb\x8d\xae\x03\xea\x01\x1b\xe1\xb6\xbb\xe1\xb5\x83\xe1\xb6\xa4\xe1\xb6\xb0\xe3\x85\xa4\xe1\xb5\x97\xe1\xb5\x89\xe1\xb5\x83\xe1\xb5\x90\xf0\x01\x01\xf8\x01\\\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0b\xd8\x02('
yout37 = b'\x06\x00\x00\x00\x8f\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x82\x01\x08\x86\xa7\x9e\xa7\x0b\x1a([18ffff]\xe2\x80\x94\xcd\x9e\xcd\x9f\xcd\x9e\xe2\x98\x85\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8[18ffff]2\x02ME@d\xb0\x01\x13\xb8\x01\xe3\x1c\xe0\x01\xf2\x83\x90\xae\x03\xea\x01!\xe3\x85\xa4\xef\xbc\xa2\xef\xbc\xac\xef\xbc\xb2\xef\xbc\xb8\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf8\x01u\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Y\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout38 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xc3\xcf\xe5H\x1a([18ffff]\xe3\x85\xa4BEE\xe2\x9c\xbfSTO\xe3\x85\xa4\xe1\xb5\x80\xe1\xb4\xb5\xe1\xb4\xb7[18ffff]2\x02ME@Q\xb0\x01\x14\xb8\x01\xffP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x15TIK\xe2\x9c\xbfTOK\xe1\xb5\x80\xe1\xb4\xb1\xe1\xb4\xac\xe1\xb4\xb9\xf0\x01\x01\xf8\x01\xc8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02q'
yout39 = b'\x06\x00\x00\x00\x94\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x87\x01\x08\x97\xd5\x9a.\x1a%[18ffff]\xd8\xb9\xd9\x86\xd9\x83\xd9\x88\xd8\xb4\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe3\x85\xa4[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xe8(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x1f\xe1\xb4\x80\xc9\xb4\xe1\xb4\x8b\xe1\xb4\x9c\xea\x9c\xb1\xca\x9c\xe3\x85\xa4\xe1\xb4\x9b\xe1\xb4\x87\xe1\xb4\x80\xe1\xb4\x8d\xf0\x01\x01\xf8\x01\xb6\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02"\xe0\x02\xf2\x94\xf6\xb1\x03'
yout40 = b'\x06\x00\x00\x00\x8a\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*~\x08\xf7\xdf\xda\\\x1a/[18ffff]\xef\xbc\xa1\xef\xbc\xac\xef\xbc\xa8\xef\xbc\xaf\xef\xbc\xad\xef\xbc\xb3\xef\xbc\xa9_\xef\xbc\xb9\xef\xbc\xb4\xe2\x9c\x93[18ffff]2\x02ME@P\xb0\x01\x13\xb8\x01\xb9*\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xc1\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\x8e\x0e\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02S\xe0\x02\xc3\xb7\xf8\xb1\x03'
yout41 = b'\x06\x00\x00\x00\x86\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*z\x08\xb5\xdd\xec\x8e\x01\x1a%[18ffff]\xd8\xa7\xd9\x88\xd9\x81\xe3\x80\x80\xd9\x85\xd9\x86\xd9\x83\xe3\x85\xa4\xe2\x9c\x93[18ffff]2\x02ME@K\xb0\x01\x13\xb8\x01\xdd#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x18\xef\xbc\xaf\xef\xbc\xa6\xe3\x85\xa4\xef\xbc\xb4\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xad\xe3\x85\xa4\xf0\x01\x01\xf8\x01\xe8\x02\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02Q'
yout42 = b'\x06\x00\x00\x00\x8b\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*\x7f\x08\x81\xf4\xba\xf8\x01\x1a%[18ffff]\xef\xbc\xa7\xef\xbc\xa2\xe3\x85\xa4\xef\xbc\xae\xef\xbc\xaf\xef\xbc\x91\xe3\x81\x95[18ffff]2\x02ME@N\xb0\x01\x0c\xb8\x01\xbd\x11\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb1\xdd\x8d\xae\x03\xea\x01\x1a\xef\xbc\xa7\xef\xbc\xb2\xef\xbc\xa5\xef\xbc\xa1\xef\xbc\xb4__\xef\xbc\xa2\xef\xbc\xaf\xef\xbc\xb9\xf8\x018\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02-\xe0\x02\x85\xff\xf5\xb1\x03'
yout43 = b'\x06\x00\x00\x00o\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*c\x08\xfb\x9d\xb9\xae\x06\x1a\x1c[18ffff]BT\xe3\x85\xa4BadroTV[18ffff]2\x02ME@@\xb0\x01\x13\xb8\x01\xe7\x1c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x91\xdb\x8d\xae\x03\xea\x01\nBadro_TV_F\xf0\x01\x01\xf8\x01\x91\x1a\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\n\xd8\x02!'
yout44 = b"\x06\x00\x00\x00s\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*g\x08\xc4\xe5\xe1>\x1a'[18ffff]\xd8\xb5\xd8\xa7\xd8\xa6\xd8\xaf~\xd8\xa7\xd9\x84\xd8\xba\xd9\x86\xd8\xa7\xd8\xa6\xd9\x85[18ffff]2\x02ME@J\xb0\x01\x14\xb8\x01\xceP\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x03Z7F\xf0\x01\x01\xf8\x01\xd0\x19\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x14\xd8\x02\x9c\x01"
yout45 = b'\x06\x00\x00\x00\x85\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*y\x08\xfd\xa4\xa6i\x1a$[18ffff]\xd8\xb2\xd9\x8a\xd9\x80\xd8\xb1\xc9\xb4\xcc\xb67\xcc\xb6\xca\x80\xe3\x85\xa4[18ffff]2\x02ME@M\xb0\x01\x13\xb8\x01\xe1(\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x19\xc2\xb7\xe3\x85\xa4\xe3\x85\xa4N\xe3\x85\xa47\xe3\x85\xa4R\xe3\x85\xa4\xe3\x85\xa4\xc2\xb7\xf0\x01\x01\xf8\x01\x8f\t\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02k'
yout46 = b'\x06\x00\x00\x00y\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*m\x08\xcc\xb9\xcc\xd4\x06\x1a"[18ffff]\xd8\xa8\xd9\x88\xd8\xad\xd8\xa7\xd9\x83\xd9\x80\xd9\x80\xd9\x80\xd9\x85[18ffff]2\x02ME@9\xb0\x01\x07\xb8\x01\xca\x0c\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x11*\xef\xbc\x97\xef\xbc\xaf\xef\xbc\xab\xef\xbc\xa1\xef\xbc\xad*\xf0\x01\x01\xf8\x01\xad\x05\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x01'
yout47 = b'\x06\x00\x00\x00e\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*Y\x08\xe8\xbd\xc9b\x1a [18ffff]\xe3\x80\x8cvip\xe3\x80\x8dDR999FF[18ffff]2\x02ME@Q\xb0\x01\x10\xb8\x01\x94\x16\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xf0\x01\x01\xf8\x01\xa0\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x0c\xd8\x02+'
yout48 = b'\x06\x00\x00\x00\x82\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*v\x08\x86\xb7\x84\xf1\x01\x1a&[18ffff]\xd8\xa2\xd9\x86\xd9\x8a\xd9\x80\xd9\x80\xd9\x84\xd8\xa7\xce\x92\xe2\x92\x91\xe3\x85\xa4[18ffff]2\x02ME@Q\xb0\x01\x13\xb8\x01\x82)\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xb2\xdd\x8d\xae\x03\xea\x01\x13\xce\x92\xe2\x92\x91\xe3\x85\xa4MAFIA\xe3\x85\xa4\xef\xa3\xbf\xf0\x01\x01\xf8\x01\x95\x04\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02W'
yout49 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout50 = b'\x06\x00\x00\x00u\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x02*i\x08\xb4\xbe\xde\x83\x02\x1a [18ffff]SPONGEBOB!\xe3\x85\xa4\xe4\xba\x97[18ffff]2\x02ME@N\xb0\x01\x14\xb8\x01\x842\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\x96\xdb\x8d\xae\x03\xea\x01\x0cALHOMSI~TEAM\xf0\x01\x01\xf8\x01\xbd\x03\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\x13\xd8\x02{'
yout51 = b'\x06\x00\x00\x00z\x08\xd4\xd7\xfa\xba\x1d\x10\x06 \x028c8d99a21bn\x08\xed\xd4\xa7\xa2\x02\x1a\x1f[18ffff]M8N\xe3\x85\xa4y\xe3\x85\xa4Fouad[18ffff]2\x02ME@O\xb0\x01\x13\xb8\x01\xa9#\xd8\x01\xd4\xd8\xd0\xad\x03\xe0\x01\xdb\xdb\x8d\xae\x03\xea\x01\x0cGREAT\xe2\x80\xbfWALL\xf0\x01\x01\xf8\x01b\x80\x02\xfd\x98\xa8\xdd\x03\x90\x02\x01\xd0\x02\r\xd8\x023\xe0\x02\xc1\xb7\xf8\xb1\x03'
yout_list = [yout1,yout2,yout3,yout4,yout5,yout6,yout7,yout8,yout9,yout10,yout11,yout12,yout14,yout15,yout16,yout17,yout18,yout19,yout20,yout21,yout22,yout23,yout24,yout25,yout26,yout27,yout28,yout29,yout30,yout31,yout32,yout33,yout34,yout35,yout36,yout37,yout38,yout39,yout40,yout41,yout42,yout43,yout44,yout45,yout46,yout47,yout48,yout49,yout50,yout51]



#################################


def likes_plus(uid, region="ME"):
    url = f"https://ff-likes-rbgx.vercel.app/like?key=RbGxLG&uid={uid}&region={region}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"""- Player : {data.get('player', 'ErRor')}
- Level : {data.get('level', 'ErRor')}
- Likes Beforr : {data.get('likes_before', 0)}
- Likes After : {data.get('likes_after', 0)}
- Likes Added : {data.get('likes_added', 0)}"""
        else:
            return f"حدث خطأ، كود الحالة : {response.status_code}"
    except Exception as e:
        return f"حدث خطأ: {e}"
        
        
        
#################################

        
def send_spam(uid):
    url = f"https://ff-spam-rbgx.vercel.app/spam?key=RbGxYh&uid={uid}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if "message" in data:  # تحقق من وجود الرسالة في الاستجابة
                return f" {data['message']}"
            else:
                return f"تم إرسال السبام إلى {uid} بنجاح !"
        else:
            return f" حدث خطأ، كود الحالة : {response.status_code}"
    except Exception as e:
        return f" حدث خطأ: {e}"
                      
               
#################################


def BesTo_msg(mess, data, clin):
    data = data[12:22]
    api_url = f"https://c4-team-generate-bb-99uyq.vercel.app/GeneRate-PaCKet-Msg?Id={data}&Msg={mess}&Key=plya-ii9ip"
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        packet = response.text
        clin.send(bytes.fromhex(packet.strip('"')))
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"    
        
                
#################################




#################################

                                
class Proxy:
    def __init__(self):
        self.username = "1"
        self.password = "1"
        self.website = "https://encrypt-id-api-rbgx.vercel.app/encrypt?id={id}"
        self.last_check_time = 0
        self.comand = True
        self.yout_list = yout_list
        self.RbGx = True
         
              
#################################

        
    def spam__invite(self, data, remote):
        global invit_spam
        while invit_spam:
            try:
                for _ in range(5):
                    remote.send(data)
                    time.sleep(0.04)
                time.sleep(0.2)
            except:
                pass
            
                                
#################################

            
    def Encrypt_ID(self, id):
        api_url = self.website.format(id=id)

        try:
            response = requests.get(api_url)
            if response.status_code == 200:
                return response.text
            else:
                print("&#1601;&#1588;&#1604; &#1601;&#1610; &#1580;&#1604;&#1576; &#1575;&#1604;&#1576;&#1610;&#1575;&#1606;&#1575;&#1578;. &#1585;&#1605;&#1586; &#1575;&#1604;&#1581;&#1575;&#1604;&#1577;:", response.status_code)
                return None
        except requests.RequestException as e:
            print("&#1601;&#1588;&#1604; &#1575;&#1604;&#1591;&#1604;&#1576;:", e)
            return None


#################################


    def handle_client(self, connection):
        version, nmethods = connection.recv(2)
        methods = self.get_available_methods(nmethods, connection)
        if 2 not in set(methods):
            connection.close()
            return
        connection.sendall(bytes([SOCKS_VERSION, 2]))
        if not self.verify_credentials(connection):
            return
        version, cmd, _, address_type = connection.recv(4)
        if address_type == 1:
            address = socket.inet_ntoa(connection.recv(4))
        elif address_type == 3:
            domain_length = connection.recv(1)[0]
            address = connection.recv(domain_length)
            address = socket.gethostbyname(address)
        port = int.from_bytes(connection.recv(2), 'big', signed=False)
        try:
            if cmd == 1:
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address, port))
                bind_address = remote.getsockname()
            else:
                connection.close()
                return
            addr = int.from_bytes(socket.inet_aton(bind_address[0]), 'big', signed=False)
            port = bind_address[1]
            reply = b''.join([
                SOCKS_VERSION.to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(0).to_bytes(1, 'big'),
                int(1).to_bytes(1, 'big'),
                addr.to_bytes(4, 'big'),
                port.to_bytes(2, 'big')
            ])
        except Exception as e:
            reply = self.generate_failed_reply(address_type, 5)
        connection.sendall(reply)
        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(connection, remote)
        connection.close()

        
#################################




    def help01(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b4646303030305d5b695d5b625d5b635d0a0a2d2057656c636f6d6520546f205262677820426f7420763720210a0a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
        



#################################




    def help02(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b4646464630305d0a2d20d985d985d98ad8b2d8a7d8aa20d988d8a7d988d8a7d985d8b120d8a7d984d8a8d988d8aa203a0a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")



#################################




    def help03(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8aed985d8b3d8a920d8a7d8b4d8aed8a7d8b520d981d98a20d8a7d984d981d8b1d98ad98220203a20205b4646464646465d0a0a2d202f3573e385a4e385a4e385a4e385a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")                    




#################################




    def help04(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c2020d8b3d8aad8a920d8a7d8b4d8aed8a7d8b520d981d98a20d8a7d984d981d8b1d98ad98220203a20205b4646464646465d0a0a2d202f3673e385a4e385a4e385a400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            


#################################




    def help05(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c2020d8b2d98ad8a7d8afd8a92031303020d984d8a7d98ad98320203a20205b4646464646465d0a0a2d202f6c696b655b69645de385a4e385a4e385a400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            



#################################




    def help06(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8b3d8a8d8a7d98520d8b7d984d8a8d8a7d8aa20d8b5d8afd8a7d982d987203a205b4646464646465d0a0a2d202f7370616d5b69645de385a4e385a4e385a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            


#################################




    def help07(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8acd988d8a7d987d8b120d988d987d985d98ad8a920203a205b4646464646465d0a0a2d202f646de385a4e385a4e385a40000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")




#################################




    def help08(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8bad988d984d8af20d988d987d985d98a20203a20205b4646464646465d0a0a2d202f676f6c64e385a4e385a4e385a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            
            



#################################




    def help09(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8a7d984d8a7d8aed8aad981d8a7d8a120d984d8a7d8b9d8a820d981d98a20d8a7d984d981d8b1d98ad982203a205b4646464646465d0a0a2d202f737079e385a4e385a4e385a400000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            
                        

#################################




    def help10(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8a7d984d8a7d8aed8aad981d8a7d8a120d984d8a7d8b9d8a820d981d98a20d8a7d984d8b1d988d985203a205b4646464646465d0a0a2d202f737079726f6de385a4e385a4e385a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            



#################################




    def help11(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8b1d982d8b5d8a7d8aa20d985d985d98ad8b2d8a9203a205b4646464646465d0a0a2d202f6131202d2d3e202f613133e385a4e385a4e385a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            
            
 

#################################




    def help12(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b625d5b635d5b3030464646465d3c20d8a7d8b6d8a7d981d8a920d98ad988d8aad98ad988d8a8d8b120d984d984d8a7d8b5d8afd982d8a7d8a1203a205b4646464646465d0a0a2d202f7974e385a4e385a4e385a4000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            
                                   


#################################




    def help13(self):
        helprbgx = f"120000018d08{self.EncryptedPlayerid}101220022a800308{self.EncryptedPlayerid}10{self.EncryptedPlayerid}22d2015b4646303030305d5b695d5b625d5b635d0a0a2d20446576204279203a2052626778205465616d204f6666696369616c0a0a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000028f0ed8db7064a3d0a18efbca2efbcb2efbcb3e385a4efbcadefbcafefbcb2efbcaf10dedd8dae031893b6d3ad0320d7012883f9f7b103420c47524f564553545249544348520261726a520a4c68747470733a2f2f67726170682e66616365626f6f6b2e636f6d2f76392e302f3132303434333431303231333534352f706963747572653f77696474683d313630266865696768743d313630100118017200"
        if self.sock1200:
            self.sock1200.send(bytes.fromhex(helprbgx))
        else:
            print("[!] sock0500 not assigned.")
            
            
#################################

        
    def gen_squad5(self, id):
        ent_packet = f"05000001ff08{id}1005203a2af20308{id}12024d451801200432f70208{id}1209424c52585f4d6f642b1a024d4520d78aa5b40628023085cbd1303832421880c38566fa96e660c19de061d998a36180a89763aab9ce64480150c90158e80792010801090a12191a1e209801c901c00101e801018802039202029603aa0208080110e43218807daa0207080f10e4322001aa0205080210e432aa0205081810e432aa0205081a10e432aa0205081c10e432aa0205082010e432aa0205082210e432aa0205082110e432aa0205081710e432aa0205082310e432aa0205082b10e432aa0205083110e432aa0205083910e432aa0205083d10e432aa0205084110e432aa0205084910e432aa0205084d10e432aa0205081b10e432aa0205083410e432aa0205082810e432aa0205082910e432c2022812041a0201041a0508501201631a060851120265661a0f0848120b0104050607f1a802f4a8022200ea0204100118018a03009203009803b7919db30ba20319c2b27854e19687e197a95fe191ade192aae197a95945e19687e20301523a011a403e50056801721e313732303237323231313638373535353930315f736f3278687a61366e347801820103303b30880180e0aecdacceba8e19a20100b00114ea010449444332fa011e313732303237323231313638373535383330335f71356f79736b3934716d"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")
            
                  

#################################



    def gen_squad6(self, id):
        ent_packet = f"050000032708{id}100520082a9a0608dbdcd7cb251a910608{id}12024d4518012005329d0508{id}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d050000031e08{id}1005203a2a910608{id}12024d4518012005329d0508{id}121ee28094cd9ecd9fcd9ee29885efbcb6efbca5efbcaeefbcafefbcade385a41a024d4520ebdd88b90628363087cbd1303832421880c38566949be061e1cea561b793e66080a89763e5bfce64480150d60158991468b7db8dae037a05ab93c5b00382011f08d1daf1eb0412054f75656973180420d487d4f0042a0808cc9d85f304100392010b0107090a0b12191a1e20229801db01a0014fc00101d001ada48aaf03e80101880203920208c205d628ae2db202aa02050801109c44aa0208080210ea3018c413aa0208080f10d836188827aa0205081710bd33aa0205082b10e432aa0205083910a070aa0205083d10c16faa02050849108439aa0205081810d836aa0205081a10d836aa0205081c10d836aa0205082010d836aa0205082210d836aa0205082110d836aa0205082310d836aa0205083110e432aa0205084110d836aa0205084d10e432aa0205081b10d836aa0205083410d836aa0205082810e432aa0205082910e432c202cd0112041a0201041a730848121301040506070203f1a802f4a802f2a802f3a8021a0b080110031886032086ac021a0b0802100418810420c59a081a0b0803100418da0620ecb4051a06080520f5ec021a0d08f1a802100318b80320def0041a0d08f2a802100318bc0520d0e90a1a0d08f3a802100318ef032092c9051a1208501201631a0b0863100e188f0420eeba0d1a1b0851120265661a09086520a6910128e7021a08086620822d289e05221f121d65ed0e890ed9049103f503ad02f90abd05e907a1068507cd08950ab109d802a6a38daf03ea020410011801f202080885cab5ee01105c8a0300920300980398e0b3af0ba20319efbca334e385a4eaa884e385a4efbcb4efbca5efbca1efbcada80368b00301c2030a081c100f180320052801e203014fea03003a011a403e50056801721e313733303239333438313635343436323834305f6c646a72387477723378880180909beaf3d18fd919a20100b001e201ea010449444331fa011e313733303239333438313635343436363239355f6f747735637831756c6d"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(ent_packet))
        else:
            print("[!] sock0500 not assigned.")




#################################



    def gen_spy(self):
        spy_packet = "0503000001d01fb578313150905babcef51dd24ed75fd0a24b024bd1429646114bc22e604afd35a96fbc48710b2d9cfec4378287ec829e33a78608fd2dd138d4d24a19c00fbfdc9f15c77ff86d638b34de95bd886e3075e82d3f4a3888f9b6943463022c43fb90e229f0eaf8a788f6f766d891d99eb2c37b277144923212810b3c80d1c521790154ed270f5241adc136f2a22816e0bc84fcaf79386b27559de966aa788c184d35bbbfaa03a5f08746f8db0e73b2c91ec4515d61f689a0cad30a7cbd6c325151e879dabc43d506b3240abe41bc0d6b4416c18f68ef4af2d04c381be6bf586f6b25727c0c85c03a579137e4a6c602ef6d833dabdab3eba3a5266e5a4731fbfb1720b60f124cd8fd4fa26cc7a9fb6e0a218d8809f57b204d22fa97520aeb99007c7b71c709e53ecc688c9963e0786909152fa93f06dc93085468dae34e1609f33f7dee228fb058c6efd6846b50ac54db0aebb8f5bc2f6751f9e2886dbab41cbaf5a1d8cd88e6c13a2a2a56b613a2d32179dc3f781493a5027322ac0cb1a2d3c79d49fb12ed26230e1561df43d315a27be17b5debdba757803305252b5443f3d77cd319dde9c49a72c636d93d02bdd9597168f378aa6e41d0fd545abf8bc0883f3dac11ea27166683c7111a0f329bf6b6a5"

        if self.sock0500:
            self.sock0500.send(bytes.fromhex(spy_packet))
        else:
            print("[!] sock0500 not assigned.")

#################################



    def gen_dm(self, player_id):
        dm_packet = f"080000001608a29b81aa22100820022a0a08e7be0110b24f18c801{player_id}"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(dm_packet))
        else:
            print("[!] sock0500 not assigned.")
    

#################################
    


    def gen_gold(self, player_id):
        gold_packet = f"080000001308{player_id}100820022a0708a6b10318fa01"
        if self.sock0500:
            self.sock0500.send(bytes.fromhex(gold_packet))
        else:
            print("[!] sock0500 not assigned.")
        
            
#################################



    def handle_spam(self, data_hex, client):
        try:
            text = str(bytes.fromhex(data_hex))
            pattern = r'/spam(\d+)'
            match = re.search(pattern, text)
            if match:
                uid = match.group(1)
                BesTo_msg(f"{generate_random_color()}\n\n- تم استقبال الايدي وجاري ارسال سبام....\n\n", data_hex, client)
                result = send_spam(uid)
                BesTo_msg(f"""{generate_random_color()}\n\n- {result} \n\n""", data_hex, client)
        except Exception as e:
            print(f"[!] Error in /spam command: {e}")
 
                       
#################################

 

    def handle_likes(self, data_hex, client):
        try:
            text = str(bytes.fromhex(data_hex))
            pattern = r'/like(\d+)'  # التعديل ليشمل "/like"
            match = re.search(pattern, text)
        
            if match:
                uid = match.group(1)
                BesTo_msg(f"{generate_random_color()}- تم استقبل الايدي وجاري ارسال 100 لايك لاغير\n\n- يرجى الانتضار....", data_hex, client)

                result = likes_plus(uid)
                BesTo_msg(f"{generate_random_color()} {result}", data_hex, client)
        except Exception as e:
            print(f"[!] Error in /likeid command: {e}")  
            
                                 


################################# 



    def gen_spyroom(self):
        spyroom_packet = "0e1500000050d6d519002bdcc64de8a42c1aaedf5c3aaacf7ce694efbfc1f11f026809b625e793614dd13ffa38eecc554ff320a61b8ac69699a8eb5edab73b39e9d9107a50d5e083a2bc8c01fbad64dbce6b8581cd50"
        if self.op:
            self.op.send(bytes.fromhex(spyroom_packet))
        else:
            print("[!] op not assigned.")
            


#################################



    def send_yout_list(self):
        if not self.sock0500:
            print("[!] sock0500 not assigned.")
            return

        for i, packet in enumerate(self.yout_list):
            try:
                self.sock0500.send(packet)
                time.sleep(0.1)
            except Exception as e:
                print(f"[!] Error sending packet {i+1}: {e}")
            


#################################

            
    def Dance(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}1088b3bbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance2(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}1098fbb8b1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance3(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}109bfbb8b1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance4(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}10d2c2bbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance5(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}10dcc2bbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance6(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}10bbfbb8b1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance7(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}109284bbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
#New
    def Dance8(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}10ff8bbbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance9(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408{self.EncryptedPlayerid}108bfbb8b1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))

    def Dance10(self):
        ent_packet = f" 050000002008c1ae939607100520162a1408{self.EncryptedPlayerid}10818cbbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance11(self):
        ent_packet = f" 050000002008c1ae939607100520162a1408{self.EncryptedPlayerid}10ca9bbbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
    def Dance12(self):
        ent_packet = f" 050000002008c1ae939607100520162a1408{self.EncryptedPlayerid}10d6c2bbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))


    def Dance13(self):
        ent_packet = f" 050000002008{self.EncryptedPlayerid}100520162a1408aae2cafb0210d7c2bbb1032a0608{self.EncryptedPlayerid}"
        self.sock0500.send(bytes.fromhex(ent_packet))
 # bot
    def garin(self):
        ent_packet = f" 050000002008c1ae939607100520162a1408{self.squad}10bdcabbb1032a0608{self.squad}"
        self.sock0500.send(bytes.fromhex(ent_packet))




#################################

    
                                
    def exchange_loop(self, client, remote):
        global inviteD
        global back
        global RbGx
        global encid
        global enc_id

        while True:
            r, w, e = select.select([client, remote], [], [])

            if client in r:
                dataC = client.recv(4096)

                if "39698" in str(remote):
                    self.op = remote
                if "39800" in str(remote):
                    self.xz = remote

                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 820 and inviteD == True:
                    for i in range(2):
                        for _ in range(5):
                            remote.send(dataC)
                            time.sleep(0.04)
                            time.sleep(0.2)

                if '0515' in dataC.hex()[0:4] and len(dataC.hex()) >= 141:
                    self.data_join = dataC

                if remote.send(dataC) <= 0:
                    break
            if remote in r:
                data = remote.recv(4096)
                



#################################



                if '1200' in data.hex()[0:4] and b'GroupID' not in data:
                        start_marker = "08"
                        end_marker = "10"
                        start_index = data.hex().find(start_marker) + len(start_marker)
                        end_index = data.hex().find(end_marker, start_index)

                        if start_index != -1 and end_index != -1:
                            enc_client_id = data.hex()[start_index:end_index]
                            self.EncryptedPlayerid = enc_client_id

                        self.squad_gen = self.Encrypt_ID(8763797454)
                        self.squad_gen5 = self.Encrypt_ID(2064377560)
                        self.squad = self.Encrypt_ID(8679231987)

                        current_time = time.time()
                        if current_time - self.last_check_time >= 60:
                            external_data = self.fetch_data_from_url()
                            if external_data and enc_client_id in external_data:
                                print("Encrypted P.")

                                self.RbGx = False
                            else:
                                print("id does not match or error fetching data.txt.")
                                self.RbGx = True
                            self.last_check_time = current_time


    


#################################

    
         
                if "0500" in data.hex()[:4]:
                    self.sock0500 = client
                if "1200" in data.hex()[:4]:
                    self.sock1200 = client
                if "0500" in data.hex()[:4]:
                    self.sock0500 = client
                    




#################################



                if '1200' in data.hex()[0:4] and b'/help' in data and not self.RbGx:

                  try:

                    threading.Thread(target=self.help01).start()
                    threading.Thread(target=self.help02).start()
                    threading.Thread(target=self.help03).start()
                    threading.Thread(target=self.help04).start()
                    threading.Thread(target=self.help05).start()
                    threading.Thread(target=self.help06).start()
                    threading.Thread(target=self.help07).start()
                    threading.Thread(target=self.help08).start()
                    threading.Thread(target=self.help09).start()
                    threading.Thread(target=self.help10).start()
                    threading.Thread(target=self.help11).start()
                    threading.Thread(target=self.help12).start()
                    threading.Thread(target=self.help13).start()


                  except Exception as e:
                      pass
                      
                      
                      
#################################

                    
                if '1200' in data.hex()[0:4] and b'/inv' in data and not self.RbGx:
                    inviteD = True
                if '1200' in data.hex()[0:4] and b'/-inv' in data and not self.RbGx:
                    inviteD = False


#################################


                if '1200' in data.hex()[0:4] and b'/5s' in data and not self.RbGx:
                
                    id = data.hex()[12:22]
                    threading.Thread(target=self.gen_squad5, args=(id,)).start()

                                        
#################################


                    
                if '1200' in data.hex()[0:4] and b'/6s' in data and not self.RbGx:
                    id = data.hex()[12:22]
                    threading.Thread(target=self.gen_squad6, args=(id,)).start()                    




#################################



                if '1200' in data.hex()[0:4] and b'/spy' in data and not self.RbGx:
                
                    threading.Thread(target=self.gen_spy).start()
                    
                    
#################################


                if b"/dm" in data and self.comand and not self.RbGx: 
                    player_id = data.hex()[12:22]
                    threading.Thread(target=self.gen_dm, args=(player_id,)).start()


#################################



                if b"/gold" in data and self.comand and not self.RbGx:
                    player_id = data.hex()[12:22]
                    threading.Thread(target=self.gen_gold, args=(player_id,)).start()



#################################



                if b"/spam" in data and self.comand and not self.RbGx:
                    threading.Thread(target=self.handle_spam, args=(data.hex(), client)).start()
 
                       
#################################
            

                if b"/like" in data and self.comand and not self.RbGx:
                    threading.Thread(target=self.handle_likes, args=(data.hex(), client)).start()
 
                       
#################################


                if b"/spyrom" in data and self.comand and not self.RbGx:
                    threading.Thread(target=self.gen_spyroom).start()
            
            
#################################



                if b"/yt" in data and not self.RbGx:
                    threading.Thread(target=self.send_yout_list).start()


#################################


            
                if '1200' in data.hex()[0:4] and b'/a1' in data and not self.RbGx:

                        threading.Thread(target=self.Dance).start()

                if '1200' in data.hex()[0:4] and b'/a2' in data and not self.RbGx:

                        threading.Thread(target=self.Dance2).start()    

                if '1200' in data.hex()[0:4] and b'/a3' in data and not self.RbGx:

                        threading.Thread(target=self.Dance3).start()    


                if '1200' in data.hex()[0:4] and b'/a4' in data and not self.RbGx:

                        threading.Thread(target=self.Dance4).start()    


                if '1200' in data.hex()[0:4] and b'/a5' in data and not self.RbGx:

                        threading.Thread(target=self.Dance5).start()    

                if '1200' in data.hex()[0:4] and b'/a6' in data and not self.RbGx:

                        threading.Thread(target=self.Dance6).start()    

                if '1200' in data.hex()[0:4] and b'/a7' in data and not self.RbGx:

                        threading.Thread(target=self.Dance7).start()    
                if '1200' in data.hex()[0:4] and b'/a8' in data and not self.RbGx:

                        threading.Thread(target=self.Dance8).start()    
                if '1200' in data.hex()[0:4] and b'/a9' in data and not self.RbGx:

                        threading.Thread(target=self.Dance9).start()

                if '1200' in data.hex()[0:4] and b'/a10' in data and not self.RbGx:

                        threading.Thread(target=self.Dance10).start()   

                if '1200' in data.hex()[0:4] and b'/a11' in data and not self.RbGx:

                        threading.Thread(target=self.Dance11).start()                   
                if '1200' in data.hex()[0:4] and b'/a12' in data and not self.RbGx:

                        threading.Thread(target=self.Dance12).start()


                if '1200' in data.hex()[0:4] and b'/a13' in data and not self.RbGx:

                        threading.Thread(target=self.Dance13).start()





#################################




                if "1200" in data.hex()[:4] and RbGx == True :
                    self.send(bytes.fromhex(gen_msgv2(data.hex() ,"[E0FF00]CHAT SPAMMER : [E0FF00]ON")))        
                if client.send(data) <= 0:
                    break
                    
                    
#################################



    def generate_failed_reply(self, address_type, error_number):
        return b''.join([
            SOCKS_VERSION.to_bytes(1, 'big'),
            error_number.to_bytes(1, 'big'),
            int(0).to_bytes(1, 'big'),
            address_type.to_bytes(1, 'big'),
            int(0).to_bytes(4, 'big'),
            int(0).to_bytes(4, 'big')
        ])


#################################


    def verify_credentials(self, connection):
        version = connection.recv(1)[0]
        username_len = connection.recv(1)[0]
        username = connection.recv(username_len).decode('utf-8')
        password_len = connection.recv(1)[0]
        password = connection.recv(password_len).decode('utf-8')


        if username == self.username and password == self.password:
            response = bytes([version, 0])
            connection.sendall(response)
            return True
        else:

            response = bytes([version, 0])
            connection.sendall(response)
            return True


#################################


    def get_available_methods(self, nmethods, connection):
        methods = []
        for _ in range(nmethods):
            methods.append(connection.recv(1)[0])
        return methods

    def run(self, ip, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((ip, port))
        s.listen()
        print(f"* Socks5 proxy server is running on {ip}:{port}")

        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=self.handle_client, args=(conn,))
            t.start()


#################################


    def RbGx(self, data_join):
        global back
        while back:
            try:
                self.op.send(data_join)
                time.sleep(9999.0)
            except Exception as e:
                pass

 
            

#################################



                                  
    def fetch_data_from_url(self):
        # weak server id's lool hhhhh 
        data_url = "https://vtbx-panel-bot-k37r.vercel.app/Uids"
        try:
            response = requests.get(data_url, verify=False)
            if response.status_code == 200:
                return response.text
            else:
                print("Failed to fetch external data. Status code:", response.status_code)
                return None
        except requests.RequestException as e:
            print("Failed to connect to external data source:", e)
            return None  


                      
 #################################

           
def gen_msgv2(packet  , replay):

    replay  = replay.encode('utf-8')
    replay = replay.hex()


    hedar = packet[0:8]
    packetLength = packet[8:10] #
    paketBody = packet[10:32]
    pyloadbodyLength = packet[32:34]#
    pyloadbody2= packet[34:60]

    pyloadlength = packet[60:62]#
    pyloadtext  = re.findall(r'{}(.*?)28'.format(pyloadlength) , packet[50:])[0]
    pyloadTile = packet[int(int(len(pyloadtext))+62):]


    NewTextLength = (hex((int(f'0x{pyloadlength}', 16) - int(len(pyloadtext)//2) ) + int(len(replay)//2))[2:])
    if len(NewTextLength) ==1:
        NewTextLength = "0"+str(NewTextLength)

    NewpaketLength = hex(((int(f'0x{packetLength}', 16) - int((len(pyloadtext))//2) ) ) + int(len(replay)//2) )[2:]
    NewPyloadLength = hex(((int(f'0x{pyloadbodyLength}', 16) - int(len(pyloadtext)//2))  )+ int(len(replay)//2) )[2:]

    finallyPacket = hedar + NewpaketLength +paketBody + NewPyloadLength +pyloadbody2+NewTextLength+ replay + pyloadTile

    return str(finallyPacket)
    
    
#################################


    
def start_bot():
    proxy = Proxy()
    proxy.run("127.0.0.1", 3000)

if __name__ == "__main__":
    start_bot()
