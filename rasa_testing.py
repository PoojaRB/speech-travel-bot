from rasa_nlu.model import Metadata, Interpreter
# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load("/models/default\model_20190224-142108")
def findIntent(queryString):
    # Prediction of Intent
    finalIntent = interpreter.parse(queryString)
    print(queryString)
    return finalIntent['intent']['name']

#print(findIntent("I would prefer a brief about it"))
    
testcases = { "Give me the rating for this place",
	"What is the rating for this place",
	"Find me the rating for this place",
   "How good is this place?",
   "How have other users rated this place?",
	"I want the rating for this place",
	"I would like to know the rating for this place",
	"Tell me the rating for this place",
	"Can you give me the rating for this place",
	"Give me their rating",
	"What is their rating",
	"Find me their rating",
	"I want their rating",
	"I would like to know their rating",
	"Tell me their rating",
	"Can you give me their rating",
	"How are the ratings for this place",
    }
for t in testcases :
     print(findIntent(t))
