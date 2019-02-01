import pyttsx3;


def synthesize(toSpeak):
    engine = pyttsx3.init();
    engine.say(toSpeak);
    engine.runAndWait() ;
        

