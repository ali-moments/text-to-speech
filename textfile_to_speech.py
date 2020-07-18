from gtts import gTTS
import os
fh = open("test.txt", "r")
myText = fh.read().replace("\n", " ")
language = 'en'
output = gTTS(text=myText, lang=language, slow=False)
output.save("output.mp3")
fh.close()
os.system("play output.mp3")
print("Done!")
