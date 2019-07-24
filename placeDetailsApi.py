import requests
import json
import datetime
import rasa_testing as rt
import speechRecognizer as sr
import speechSynthesizer as ss
import distance as distFinder
import math
import wikipedia
import sys


def truncate(number, digits) -> float:
    stepper = pow(10.0, digits)
    return math.trunc(stepper * number) / stepper


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

days = {
       "Monday": 1 ,
       "Tuesday": 2 ,
       "Wednesday": 3,
       "Thursday": 4 ,
       "Friday": 5,
       "Saturday": 6,
       "Sunday": 0
        }


def getFilteredDetails(placeId):
    ss.synthesize("What would you like to know about this place")
    response = sr.recognize()
    if response == None:
        getFilteredDetails(placeId)
    else:
        intent = rt.findIntent(response)
        #print(intent)
        if intent in filter_list :
            reqURL = ('https://maps.googleapis.com/maps/api/place/details/json?placeid='+placeId+'&key='+api_key)
            response = requests.get(reqURL)
            result = json.loads(response.content.decode('utf-8'))
            r = result['result']
            #print(r['name'])
            getPlaceDetails(placeId,r,intent)
            ss.synthesize("Do you want to know anything more (yes/no)")
            response = sr.recognize()
            if response == "yes":
                getFilteredDetails(placeId)
            else:
                ss.synthesize("Thank you") 
                exit
        else :
            ss.synthesize("Sorry we dont have these details, ask something else!")
            getFilteredDetails(placeId)


def getPlaceDetails(placeId,r,intent):
    try:
        if intent == "summary":
            var = r['name']
            try :
                ss.synthesize(wikipedia.summary(var, sentences=1, auto_suggest=False))
            except wikipedia.exceptions.PageError:
                ss.synthesize("Sorry we do not have summary for "+var)
                getFilteredDetails(placeId)
        elif intent == "address":
            ss.synthesize("The address of this place is "+ r['formatted_address'] )
        elif intent == "phone":
            ss.synthesize("The contact number is "+r['international_phone_number'])
        elif intent == "rating":
            ss.synthesize("THis place is rated "+str(r['rating']))
        elif intent == "opening_hours":
            time = getOpeningDetails(r)
            if time == None:
                ss.synthesize("Sorry this place is closed today")
            else:
                ss.synthesize("The working hours for today are "+time )        
        elif intent == "price":
            ss.synthesize("The price range is " + price_dict[r["price_level"]])
        elif intent == "distance":
            lati=r['geometry']['location']['lat']
            lngi=r['geometry']['location']['lng']
            finalDist = distFinder.distance((lati,lngi))
            f=truncate(finalDist,3)
            ss.synthesize("The distance from here is "+ str(f) + " kilometers")
        elif intent == "website":
            ss.synthesize("The Website is "+  r['website'])
        else :
            ss.synthesize("Sorry your query is invalid")
            getFilteredDetails(placeId)
    except KeyError :
        ss.synthesize("The details related to "+intent+" are not available")
        getFilteredDetails(placeId)


def getOpeningDetails(r):
    currentDay = datetime.datetime.now().strftime("%A")
    print(currentDay)
    daysDetails = r['opening_hours']['weekday_text']
    for x in daysDetails:
        if str(x).find(currentDay) != -1:
            if str(x).find("Closed") != -1 :
                return None
            else:
                y=str(x).replace('–','to')
                time = y.split(' ', 1)[-1]
                return time
 
            
    

#getFilteredDetails("ChIJU3TYU3FnUjoRB-aq_tlGV7Q")
    
   