
def getBusinessType(nou):
    print(nou)
    categories = {
            "bakery":["bakery","bakery_search","bakeries"],
            "cafe" : ["Cafe","Cafes","cafe","cafe_search"],
            "church" : ["Churches","Church","church","church_search"],
            "hindu_temple" : ["temple","temples","temple_search"],
            "lodging" : ["hotels","hotel","place to stay","lodging_search"],
            "restaurant" : ["restaurants","Restaurants","restaurant_search"],
            "mosque" : ["Mosque","mosque_search","mosques","mosque"],
            "movie_theater" : ["theater","movie","theatre","theatres","theaters","movies"],
            "shopping_mall" : ["mall","shopping"],
            "place_of_worship" : ["worship","place of worship","worship_search"],
            "zoo" : ["zoo","zoos"],
            "pharmacy" : ["pharmacies","pharmacy_search"],
            "supermarket" : ["Supermarkets","supermarket","supermarket_search"],
            "atm" : ["atms","ATM","ATMs"],
            "beach" : ["beaches","beach"],
            "museum" : ["museum","museum_search"],
            "park" : ["park","park_search"] 
            }
    
    key = ''
    for k in categories.keys() : # getting all the keys
        if k == nou :
            return k
        else:
            for v in categories.get(k): #for particular key get each value
                if v == nou : 
                    #print(k)
                    key = k
                    return key
    #print(categories.items())   