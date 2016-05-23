import zipfile
zFile = zipfile.ZipFile("2.zip")
passFile = open("dictionary.txt")

def extractFile(zFile,password):
	#print password
	try:
		zFile.extractall(pwd=password)
		#print "password is :"+password+"\n"
		return password
	except Exception,e:
		#print password
		pass
		#print e

def main():
	for line in passFile.readlines():
	#password = line.strip('\n')
		password = line.strip('\n')
		guess = extractFile(zFile,password)
		if guess != None:
			print '[+] password = :' +password+ '\n'
			exit(0)
		#print guess

if __name__ == "__main__":
	main()

