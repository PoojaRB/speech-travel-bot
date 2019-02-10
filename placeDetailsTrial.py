import requests
import json
import time

api_key = 'AIzaSyCh2R-XGeUDY5yE_JeqYvujkq8ku8Bi9ZE' #You'll need your own API key: https://developers.google.com/places/web-service/get-api-key
def findThePlaces(domainName): 
    total_results = []
    
    def get_nearby_places(coordinates, business_type, next_page):
        URL = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+coordinates+'&radius=4000&key='+ api_key +'&type='+business_type+'&pagetoken='+next_page)
        r = requests.get(URL)
        response = r.text
        python_object = json.loads(response)
        results = python_object["results"]
        for result in results:
            #place_name = result['name']
            place_id = result['place_id']
            get_place_details(place_id)
        try:
            next_page_token = python_object["next_page_token"]
        except KeyError:
    		#no next page
            return
        time.sleep(1)
        get_nearby_places(coordinates, business_type, next_page_token)
    
    def get_place_details(place_id):
        reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&key='+api_key)
        r = requests.get(reqURL)
        response = r.text
        #python_object = json.loads(response)
        resultm = json.loads(response)
        try:
            #result = python_object['result']
            result = resultm['result']
            place_name = result['name']
            if 'rating' in result:
                rating = result['rating']
            else:
                rating = "none"
            if 'formatted_address' in result:
                priceLevel = result['formatted_address']
            else:
                priceLevel = "none"
            total_results.append([place_name,rating,priceLevel])
            print([place_name,rating,priceLevel])
        except Exception as e:
            print(str(e))
        return
    
    get_nearby_places('12.7517236,80.1968122', domainName , '')
    return total_results
    
        
findThePlaces('lodging')