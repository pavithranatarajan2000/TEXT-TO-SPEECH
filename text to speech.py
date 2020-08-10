import pyttsx3
test = "Hii Friends!!!! Happy friendship day to all"
engine = pyttsx3.init()
#voices = engine.getProperty('voices')
en_voice_id = "com.apple.speech.synthesis.voice.Alex"
engine.setProperty('voice', en_voice_id)
engine.say(test)
engine.runAndWait()
