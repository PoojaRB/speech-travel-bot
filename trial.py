import speechSynthesizer 
import speechRecognizer
import spacy
import placeApi

total_results= []
i=1
nou=''
nlp = spacy.load('en')
toSpeak=speechRecognizer.recognize()
doc = nlp(toSpeak)
for token in doc:        #for getting each word
   if token.pos_ == "NOUN":
        print(token.text,token.pos_)
        nou=token.text;
        print(nou)
total_results=placeApi.findThePlaces(nou)
for t in total_results:
    if i < 11 :
        tname= str(t[1])
        trating= str(t[2])
        tvicinity=str(t[3])
        toSpeak = tname+" at "+tvicinity+" with rating "+trating
        print(toSpeak)
        speechSynthesizer.synthesize(toSpeak)
        i+=1
#placeApi.findThePlaces("restaurant")church lodging bakery cafe zoo park 
#speechSynthesizer.synthesize(toSpeak)

#check
