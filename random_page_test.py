import random
from dpla.api import DPLA 
from credentials import *

#create DPLA object using dpla module and API key
dpla = DPLA(DPLA_KEY)

#generate a random number to use as the page value
random_page = random.randint(1, 100)

#create results set of all DPLA items where provider is SSDN 
fields = {"provider" : "Sunshine State Digital Network"}
result = dpla.search(searchFields=fields, page_size=10, page=random_page)

#print title and identifier of results from API call
for item in result.items:
	title = item["sourceResource"]["title"]
	identifier = item["@id"]
	
	print(title)
	print(identifier)
	