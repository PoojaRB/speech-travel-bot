from rasa_nlu.model import Metadata, Interpreter
# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load("/models/default\model_20190305-193608")
def findIntent(queryString):
    # Prediction of Intent
    finalIntent = interpreter.parse(queryString)
    return finalIntent['intent']['name']

##listtest ={
        #"Can you brief me about the place ",
#"Can you brief me about this place",
#"Can you brief me about that place",
#"Can you brief me about it",
#"I want some details about it",
#"I want some details about the place",
#"I want some details about that place",
#"I want some details about this place",
#"Give me details",
#"Give me details about it",
#"Give me details about this place",
#"Give me details about that place",
#"Give me details about the place",
#"I would like some details about this place",
#"I would like some details about that place",
#"I would like some details about the place",
#"I would like some details about it",
#"I would like a brief about this place",
#"I would like a brief about that place",
#"I would like a brief about the place",
#"I would like a brief about it",
#"I would like to know some information about that place",
#"I would like to know some information about the place",
#"I would like to know some information about it",
#"I would like to know some information about this place",
#
#}
#
#for x in listtest:
    #print(x+ ":" +findIntent(x))
#
