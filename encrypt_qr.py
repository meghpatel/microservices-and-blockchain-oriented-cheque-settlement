import pyqrcode 
from pyqrcode import QRCode
import random
import sqlite3
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

a0='0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1'
a1='0xFFcf8FDEE72ac11b5c542428B35EEF5769C409f0'
a2='0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b'
a3='0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d'
a4='0xd03ea8624C8C5987235048901fB614fDcA89b117'
a5='0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC'
a6='0x3E5e9111Ae8eB78Fe1CC3bb8915d5D461F3Ef9A9'
a7='0x28a8746e75304c0780E011BEd21C72cD78cd535E'
a8='0xACa94ef8bD5ffEE41947b4585a84BdA5a3d3DA6E'
a9='0x1dF62f291b2E969fB0849d99D9Ce41e2F137006e'

addr_list=[a0,a1,a2,a3,a4,a5,a6,a7,a8,a9]

def create_save(acc_number):
	print("Heyy you called me!!!!!!!!!!!!!!!")
	conn=sqlite3.connect('database.db')
	c=conn.cursor()
	c.execute('select * from user_qr')
	temp=c.fetchall()
	try:
		para1=len(temp)+1
	except:
		para1=1
	print(para1)
	para2=random.choice(addr_list)
	cipher = encrypt(para1,para2)
	encoded_cipher = str(b64encode(cipher))
	
	c.execute('insert into user_qr values (?,?,?,"available")',(para1,encoded_cipher,acc_number))
	conn.commit()
	print("GENERATED!!")
	qr_path="static/qr/_"+str(para1)+".png"
	url = pyqrcode.create(encoded_cipher)
	url.png(qr_path, scale = 8)

	print(encoded_cipher)
	print(type(encoded_cipher))

if __name__ == '__main__':
	create_save(1234567880)