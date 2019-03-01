import requests
import json
import time


#business_types = [


#]
api_key = 'AIzaSyCh2R-XGeUDY5yE_JeqYvujkq8ku8Bi9ZE' #You'll need your own API key: https://developers.google.com/places/web-service/get-api-key
def findThePlaces(domainName): 
    total_results = []
    print("hejjkledkfjndjcdnsjddmjkfmkfj")
    def get_nearby_places(coordinates, business_type, next_page):
    	URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='
    		+coordinates+'&radius=10000&key='+ api_key +'&type='
    		+business_type+'&pagetoken='+next_page)
    	r = requests.get(URL)
    	response = r.text
    	python_object = json.loads(response)
    	results = python_object["results"]
    
    	for result in results:
            place_name = result['name']
            if 'rating' in result:
                rating = result['rating']
            else:
                rating = "not available"
            if 'vicinity' in result:
                vicinity = result['vicinity']
            else:
                vicinity = "not available"
            place_id = result['place_id']
            #website = get_place_website(place_id)
            #print([business_type, place_name,vicinity,rating,place_id])
            total_results.append([business_type, place_name,rating,vicinity,place_id])
    	try:
    		next_page_token = python_object["next_page_token"]
    	except KeyError:
    		#no next page
    		return
    	time.sleep(1)
    	get_nearby_places(coordinates, business_type, next_page_token)
    
    
    
    get_nearby_places('12.751587, 80.203681', domainName , '')
  #  get_nearby_places('9.922209, 78.115099', domainName , '')
    
    return total_results
#findThePlaces("hindu_temple")