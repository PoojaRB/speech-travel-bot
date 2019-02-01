import speechSynthesizer 
import speechRecognizer
import spacy
import placeApi

nlp = spacy.load('en')
toSpeak=speechRecognizer.recognize()
doc= nlp(toSpeak)
for token in doc:        #for getting each word
    if token.pos_ == "NOUN":
        print(token.text,token.pos_)
        nou=token.text;
        print(nou)
placeApi.findThePlaces('supermarket')
#placeApi.findThePlaces("restaurant")
speechSynthesizer.synthesize(toSpeak)

#check
