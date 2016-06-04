import pygeoip,dpkt,socket
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	city = rec['city']
	region = rec['city']
	country = rec['country_name']
	long_long = rec['longitude']
	lat = rec['latitude']
	#if city == "":
	#	return 
	print '[*] Target: ' +tgt+ ' Geo-located.'
	print '[+] ' +str(city)+ ', ' + str(region)+ ', ' +str(country)
	print '[+] Latitude: '+str(lat)+', Longitude: '+str(long_long)

def printPcap(pcap):
	for (ts,buf) in pcap:
		try:
			eth = dpkt.ethernet.Ethernet(buf)
			ip = eth.data
			src = socket.inet_ntoa(ip.src)
			dst = socket.inet_ntoa(ip.dst)
			print '[+] Src: ' +src
			#printRecord(src)
			print '---> Dst: ' +dst
			#printRecord(dst)
			print '\n'
		except Exception,e:
			pass
def main():
	f = open('a.pacp')
	pcap = dpkt.pcap.Reader(f)
	printPcap(pcap)

if __name__ == "__main__":
	main()
