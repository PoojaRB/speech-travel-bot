import requests
import json
import time


#business_types = [


#]
api_key = '' #You'll need your own API key: https://developers.google.com/places/web-service/get-api-key
def findThePlaces(domainName): 
    total_results = []
    
    def get_nearby_places(coordinates, business_type, next_page):
    	URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    		+coordinates+'&radius=16093&key='+ api_key +'&type='
    		+business_type+'&pagetoken='+next_page)
    	r = requests.get(URL)
    	response = r.text
    	python_object = json.loads(response)
    	results = python_object["results"]
    
    	for result in results:
    		place_name = result['name']
    		#place_id = result['place_id']
    		#website = get_place_website(place_id)
    		print([business_type, place_name])
    		total_results.append([business_type, place_name])
    	try:
    		next_page_token = python_object["next_page_token"]
    	except KeyError:
    		#no next page
    		return
    	time.sleep(1)
    	get_nearby_places(coordinates, business_type, next_page_token)
    
    
    
    get_nearby_places('12.7517236,80.1968122', domainName , '')
    
    return total_results
#findThePlaces("restaurant")