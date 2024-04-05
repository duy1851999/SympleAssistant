import speech_recognition
from gtts import gTTS
import os
robot_brain=""
robot_ear=speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
    audio=robot_ear.listen(mic)
try:
    you=robot_ear.recognize_google(audio,Language='vi-VN')
except:
    you="I don't here"
if you=="Xin chào":
    robot_brain="chào Duy"
tts=gTTS(text=robot_brain,Lang='vi')
tts.save("pcvoice.mp3")
os.system("start pcvoice.mp3")
