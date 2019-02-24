import requests
import json

api_key = 'AIzaSyCh2R-XGeUDY5yE_JeqYvujkq8ku8Bi9ZE' #You'll need your own API key: https://developers.google.com/places/web-service/get-api-key

def get_place_details(place_id):
    reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='+place_id+'&key='+api_key)
    response = requests.get(reqURL)
    result = json.loads(response.content.decode('utf-8'))
    r = result['result']
    print(r['name'])
        
get_place_details('ChIJFe9d9S9RUjoR1dbX_IJNT1w')
    
   