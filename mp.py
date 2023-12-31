from gtts import gTTS
from playsound import playsound

s = gTTS("sann nii ichii")

s.save('sample.mp3')
playsound('sample.mp3')
