import welcome
import encode_password
import hashlib
import getpass
import decode_flag

with open('password.txt', 'r') as f:
	password = f.readline().split()[2]

givenPassword = getpass.getpass("\nPlease enter the password to verify you are the devil: ")

givenPasswordHash = hashlib.md5(givenPassword).hexdigest()

if givenPasswordHash != password:
	print "\nSorry, you are not the devil. Only the devil can destroy the world..."
else:
	print "\nThe world will be destroyed soon!!!"
	print "\nHere is the flag to stop the distortion: "
	with open('flag.txt', 'r') as f:
		flag = f.read()
	print decode_flag.decode(flag,givenPassword)