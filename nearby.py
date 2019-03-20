import speechSynthesizer 
import speechRecognizer
import placeApi
import dict

def findNearbyPlace(nou):
    total_results= []
    i=1
    x=1
    ch=0
    btype = dict.getBusinessType(nou)
    #print(btype)
    if btype == None :
        speechSynthesizer.synthesize("I am sorrry we do not have details for this place yet")
        return None
    else :
        total_results=placeApi.findThePlaces(btype)
        for t in total_results:
            if i < 6 :
                tname= str(t[1])
                #tvicinity=str(t[3])
                tvicinity = str(t[3]).split(",")
                try:
                    v=tvicinity[-2]
                except IndexError:
                    v=tvicinity[-1]
                toSpeak = str(x)+". "+tname+" at "+ v
                speechSynthesizer.synthesize(toSpeak)
                x+=1
                i+=1
        speechSynthesizer.synthesize("Choose one of the places. (Specify the number)")
        ch = getChoice()
        #print(ch)
        print(total_results[ch-1][1])
    return total_results[ch-1][4]
                        
                
def getChoice():
        try:
            num = speechRecognizer.recognize()
            rep = int(num)
            if rep > 5:
                speechSynthesizer.synthesize("Invalid choice.. please choose again")
                return getChoice()
            else:
                return rep
        except ValueError :
            speechSynthesizer.synthesize("repeat your choice")
            return getChoice()
        except TypeError :
            speechSynthesizer.synthesize("repeat your choice")
            return getChoice()
        
#findNearbyPlace("zoo")
#church lodging bakery cafe zoo park 

