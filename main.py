from gtts import gTTS
import os 

test_text = 'hello this is a test'
language = 'en' 

tts = gTTS(text=test_text,lang=language)

tts.save("test.mp3")
os.system("test.mp3")