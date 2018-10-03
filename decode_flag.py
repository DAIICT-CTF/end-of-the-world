def decode(flag,password):
	password = password*100
	return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(flag,password))