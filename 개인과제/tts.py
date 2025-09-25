from gtts import gTTS
import os

text = "파이썬 재밌다"

tts = gTTS(text=text, lang='ko')
tts.save('ttt.mp3')
os.system("../ex4/ttt.mp3")
