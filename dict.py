
def getBusinessType(nou):
    categories = {
            "cafe" : ["Cafe","Cafes"],
            "church" : ["Churches","Church","church","church_search"],
            "hindu_temple" : ["temple","temples","temple_search"],
            "lodging" : ["hotels","hotel","place to stay"],
            "restaurant" : ["restaurants","Restaurants","restaurant_search"],
            "mosque" : ["Mosque","mosque_search"],
            "movie_theater" : ["theater","movie","theatre"],
            "shopping_mall" : ["mall","shopping"],
            "place_of_worship" : ["worship","place of worship","worship_search"]
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