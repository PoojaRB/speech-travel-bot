from rasa_nlu.model import Metadata, Interpreter
# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load("/models/default\model_20190228-100329")
def findIntent(queryString):
    # Prediction of Intent
    finalIntent = interpreter.parse(queryString)
    return finalIntent['intent']['name']

print(findIntent("Give me the price"))
    

