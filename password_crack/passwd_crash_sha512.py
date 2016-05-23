import hashlib

def crash(cryptPass):
	dictFile = open("dictionary.txt",'r')
	#passFile = open("password.txt",'r')

	#print dictFile
	for word in dictFile.readlines():
		word = word.strip('\n')
		#print word
		passwd_f = hashlib.sha512(word).hexdigest()
		print "a:"+passwd_f
		print "b:"+cryptPass
		passwd_f = "$6$"+passwd_f
		if passwd_f == cryptPass:
			print "[+] Found password :"+passwd_f+"\n"
			return
	#print "[-] Password not found.\n"

def main():
	passFile = open("password.txt")
	for line in passFile.readlines():
		if ":" in line:
			user = line.split(':')[0]
			cryptPass = line.split(":")[1].strip()
			print "------------"+cryptPass
			#print "[*] Cracking Password for uaer :" +user
			crash(cryptPass)
if __name__ == "__main__":
	main()
