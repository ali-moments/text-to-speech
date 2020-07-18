from gtts import gTTS 
import os 
mytext = input("Enter something to convert to speech: \n")
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False) 
myobj.save("output.mp3") 
os.system("play output.mp3") 
print("Done!")
