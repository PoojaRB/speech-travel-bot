import pyttsx3;


def synthesize(toSpeak):
    engine = pyttsx3.init();
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty('voice', en_voice_id)
    engine.setProperty('rate', 180)
    engine.say(toSpeak);
    engine.runAndWait() ;
    
synthesize('Gents UG Mess. AA RENTALS at Kalavakkam with rating 2.5')
        

