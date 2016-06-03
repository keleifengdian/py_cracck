import ftplib
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostnaem)
		ftp.login("uftp","111111")
		print "\n[*]" +str(hostname) +\
			  "FTP Anonymous Login Succeeded"
		ftp.quit()
		return True
	except Exception, e:
		print "\n[-] " +str(hostname) +\
			'FTP Anonymous Login Failed'
		return False

host = "192.168.72.128"
anonLogin(host)
