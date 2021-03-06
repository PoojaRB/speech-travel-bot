
import pyttsx3;
import speech_recognition as sr
import spacy


nlp = spacy.load('en')
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Speak")
    audio = r.listen(source)
try:
    print("You said " + r.recognize_google(audio));
    doc= nlp(r.recognize_google(audio))
#    for sent in doc.sents:
    for token in doc:        #for getting each word
            if token.pos_ == "NOUN":
                print(token.text,token.pos_)
    for word in doc.ents:
            print("value",word.text,"entity",word.label_,"start",word.start_char,"end",word.end_char)
    engine = pyttsx3.init();
    engine.say("You said " + r.recognize_google(audio));
    engine.runAndWait() ;
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))



