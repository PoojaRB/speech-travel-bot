import speech_recognition as sr

def recognize():
    #print("Speak")
    r = sr.Recognizer()
    youSaid = None
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        print("USER: " + r.recognize_google(audio));
        youSaid= r.recognize_google(audio)
        return youSaid
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    

