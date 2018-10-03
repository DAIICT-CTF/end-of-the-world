import hashlib

with open('password.txt', 'r') as f:
	line = f.readline()
	passwordState = line.split()[0]
	password = line.split()[2]

if passwordState == 'PlainPassword':
	with open('password.txt', 'w') as f:
		f.write("EncodedPassword : " + hashlib.md5(password).hexdigest())

	print "Successfully encoded the password..."