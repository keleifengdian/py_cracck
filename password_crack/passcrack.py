import crypt
def	testPass(cryptPass):
	salt = cryptPass[0:12]
	#print "ccccccccccccccc---"+cryptPass
	dictFile = open('mutou.txt','r')
	for word in dictFile.readlines():
		word = word.strip('\n')
		cryptWord = crypt.crypt(word,salt)
		#print "ssssssssssssss----"+salt
		if word == "111111":	
			print word
		if (cryptWord == cryptPass):
			print "[+] Found passwd: "+word+"\n"
			return
	print "[-] passwd not found.\n"
	return

def main():
	passFile = open("password.txt",'r')
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(':')[1].strip(' ')
			print "[*] Cracking Password for : " +user
			testPass(cryptPass)

if __name__ == "__main__":
	main()
