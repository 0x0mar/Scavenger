#!/usr/bin/env python
__author__ = "Jared Stroud"

class Shodan:

	def srchShodan(search_term):
		results = api.search(search_term) #searching based on users preset terms
		print (shosearch, 'resulted in %s results' % results ['total'])
		
		for result in results ['matches']:
			print 'IP: %s' % result['ip'] #printing searches API
			print result['data'] #Printing informaton from banners
			print ''

#Name: shodanHost
#Function: searches IP address, country info, banners, ports etc...
	def shodanHost(ip):

		host = api.host(ip) #looks up geo location (sometimes will throw back "none" if nothing is recorded in database"
		
		print """ 
			IP: %s
			Country: %s
			City: %s
			\n
			""" %(host['ip'], host.get('country', None), host.get('city',None)) #Printing geo location
		


