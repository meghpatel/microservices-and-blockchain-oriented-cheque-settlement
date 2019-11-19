import sys
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass
password = getpass()
encoded_cipher = sys.argv[1]
cipher = b64decode(encoded_cipher)
plaintext = decrypt(password, cipher)
print(plaintext)
