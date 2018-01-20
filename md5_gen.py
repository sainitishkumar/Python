import hashlib,sys

def md5gen(password):
	md5hash = hashlib.md5()
	md5hash.update(password.encode('ascii'))
	return md5hash.hexdigest()

password = str(sys.argv[1])
print(md5gen(md5gen(password)))