# TEXT-TO-SPEECH

Here whatever the text given will converted to as speech
Here we can choose voice and language

Just type it in the terminal to get the voices and language

engine = pyttsx3.init()  
voices = engine.getProperty('voices')
for voice in voices:
 print("Voice:")
 print(" - ID: %s" % voice.id)
 print(" - Name: %s" % voice.name)
 print(" - Languages: %s" % voice.languages)
 print(" - Gender: %s" % voice.gender)
 print(" - Age: %s" % voice.age)
