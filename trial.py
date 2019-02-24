import speechRecognizer as sr
import spacy
import nearby
import speechSynthesizer as ss
import time
import rasa_testing as rt

temp = "What type of place do you want to visit?"
ss.synthesize(temp)
placeId = nearby.findNearbyPlace()
print(placeId)
askUser = "Do you want a brief about the place or any specific details?"
ss.synthesize(askUser)
response = sr.recognize();
intent = rt.findIntent(response)
print(intent)

    

    
