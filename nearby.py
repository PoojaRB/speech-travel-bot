import speechSynthesizer 
import speechRecognizer
import spacy
import placeApi
import dict
import rasa_testing as rt

def findNearbyPlace():
    total_results= []
    i=1
    x=1
    nou=''
    nlp = spacy.load('en')
    print("Speak")
    toSpeak=speechRecognizer.recognize()
    #doc = nlp(toSpeak)
    #for token in doc:        #for getting each word
     #  if token.pos_ == "NOUN":
      #      print(token.text,token.pos_)
       #     nou=token.text;
        #    print(nou)
    nou=rt.findIntent(toSpeak)
    print("INTENT OUTPUT:"+nou)
    btype = dict.getBusinessType(nou)
    print(btype)
    if btype == None :
        speechSynthesizer.synthesize("I am sorrry we do not have details for this place yet")
    else :
        total_results=placeApi.findThePlaces(btype)
        for t in total_results:
            if i < 6 :
                tname= str(t[1])
                trating= str(t[2])
                tvicinity=str(t[3])
                toSpeak = str(x)+". "+tname+" at "+tvicinity+" with rating "+trating
                speechSynthesizer.synthesize(toSpeak)
                x+=1
                i+=1
        speechSynthesizer.synthesize("Choose one of the places. (Specify the number)")
        print("Speak")
        rep = int(speechRecognizer.recognize())
        print(total_results[rep-1][1])
    return total_results[rep-1][4]
        
#placeApi.findThePlaces("restaurant")church lodging bakery cafe zoo park 
#speechSynthesizer.synthesize(toSpeak)

#check
