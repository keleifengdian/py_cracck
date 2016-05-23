import optparse
from socket import *

def connScan(tgtHost,tgtPorts):
	try:
		connSkt = socket(AF_INET,SOCK_STREAM)
		connSkt.connect((tgtHost,tgtPorts))
		print '[+] %d /tcp open' %tgtPorts
		connSkt.close();
	except:
		print '[-]%d /tcp closed'%tgtPorts

def portScan(tgtHost,tgtPorts):
	try:
		tgtIP = gethostbyname(tgtHost)
	except:
		print "[-] Cannot resolve '%s': Unknown host" %tgtHost
		return
	try:
		tgtName = gethostbyaddr(tgtIP)
		print '\n[+] Scan Results for : '+tgtName[0]
	except:
		print '\n[+] Scan Results for:' +tgtIP
	setdefaulttimeout(1)
	for tgtPort in range(int(tgtPorts[0]),int(tgtPorts[1])):
		print 'Scanning port %d' %tgtPort
		connScan(tgtHost,int(tgtPort))

def main():
	parser = optparse.OptionParser("usage %prog -H"+\
		'<target host> -p <target port>')
	parser.add_option('-H',dest='tgtHost', type='string',\
		help='specify target host')
	parser.add_option('-p',dest = 'tgtPort',type='string',\
		help='specify target port[s] separated by comma')
	(options,args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split('/')
	if (tgtHost == None) | (tgtPorts[0] == None):
		print parser.usage
		exit(0)
	#for ports in tgtPorts:
		#print ports
	portScan(tgtHost,tgtPorts)

if __name__ == '__main__':
	main()
