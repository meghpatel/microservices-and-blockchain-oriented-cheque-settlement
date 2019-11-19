import pyqrcode
import sys
import hashlib
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass
password = getpass()
message = sys.argv[1]
cipher = encrypt(password, message)
encoded_cipher = b64encode(cipher)
print(encoded_cipher)
# file1 = open("encrypted_string_details.txt","a")
# L=[message+"\t"+encoded_cipher+"\n"]
# file1.writelines(L)
# file1.close()
# qrkey = pyqrcode.create(encoded_cipher, error='H')
# print ("Creating QR code")
# qrkey.png('outputQR/'+message+'.png', scale=5)
