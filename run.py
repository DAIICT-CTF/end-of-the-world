import welcome
import encode_password
import hashlib
import getpass

with open('password.txt', 'r') as f:
	password = f.readline().split()[2]

givenPassword = getpass.getpass("\nPlease enter the password to verify you are the devil: ")

givenPassword = hashlib.md5(givenPassword).hexdigest()

if givenPassword != password:
	print "\nSorry, you are not the devil. Only the devil can destroy the world..."
else:
	print "\nThe world will be destroyed soon!!!"