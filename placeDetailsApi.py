import requests
import json
import rasa_testing as rt
import speechRecognizer as sr
import speechSynthesizer as ss

api_key = 'AIzaSyCh2R-XGeUDY5yE_JeqYvujkq8ku8Bi9ZE'
filter_list={"summary",
"address",
"phone",
"rating",
"opening_hours",
"price",
"distance",
"website" }

price_dict = {
        1 : "very cheap",
        2 : "cheap",
        3 : "moderate",
        4 : "not very expensive",
        5 : "expensive"
        }


def getFilteredDetails(placeId):
    ss.synthesize("What would you like to know about this place")
    response = sr.recognize();
    intent = rt.findIntent(response)
    print(intent)
    if intent in filter_list :
        reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeId+'&key='+api_key)
        response = requests.get(reqURL)
        result = json.loads(response.content.decode('utf-8'))
        r = result['result']
        print(r['name'])
        getPlaceDetails(placeId,r,intent)
    else :
        ss.synthesize("Sorry we dont have these details, ask something else!")
        getFilteredDetails(placeId)


def getPlaceDetails(placeId,r,intent):
    try:
        if intent == "address":
            ss.synthesize("The address of this place is "+ r['formatted_address'] )
        elif intent == "phone":
            ss.synthesize("The contact number is "+r['international_phone_number'])
        elif intent == "rating":
            ss.synthesize("THis place is rated "+str(r['rating']))
        elif intent == "opening_hours":
            ss.synthesize("It opens at")
        elif intent == "price":
            ss.synthesize("The price range is " + price_dict[r["price_level"]])
        elif intent == "distance":
            ss.synthesize("The distance from here is ")
        elif intent == "website":
            ss.synthesize("The Website is "+  r['website'])
        else :
            ss.synthesize("Sorry your query is invalid")
            getFilteredDetails(placeId)
    except KeyError :
        print("The details related to "+intent+" are not available")

    
  

getFilteredDetails("ChIJZzVWjUZmUjoR6nrLPiuavZo")
    
   