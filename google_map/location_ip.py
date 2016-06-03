import pygeoip
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
	rec = gi.record_by_name(tgt)
	print rec
	city = rec['city']
	region = rec['city']
	country = rec['country_name']
	long_long = rec['longitude']
	lat = rec['latitude']
	print '[*] Target: ' +tgt+ ' Geo-located.'
	print '[+] ' +str(city)+ ', ' + str(region)+ ', ' +str(country)
	print '[+] Latitude: '+str(lat)+', Longitude: '+str(long_long)
tgt = "8.8.8.8"
printRecord(tgt)
