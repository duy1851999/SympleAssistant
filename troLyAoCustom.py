import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime
from gtts import gTTS
import os
import playsound
# import locale
# locale.setlocale(locale.LC_CTYPE, 'chinese')
i=0
robot_ear=speech_recognition.Recognizer()
#robot_mouth = pyttsx3.init()
#robot_brain=""
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm Listening")
        audio = robot_ear.record(mic, duration=3)
        robot_ear.adjust_for_ambient_noise(mic)
        audio=robot_ear.listen(mic)# Dung viet
        #robot_ear.adjust_for_ambient_noise(mic)
        #audio = robot_ear.record(mic, duration=5)

    print("Robot: ...")
    try:
        #you = robot_ear.recognize_google(audio)
        you=robot_ear.recognize_google(audio,language='vi')
    except:
        you=""
    print("You: "+you)
    if you=="":
        robot_brain="Tôi không nghe rõ"
    elif ("xin chào" in you) or ("Xin chào" in you):
        robot_brain="Hello Duc Duy"
    elif "hôm nay" in you:
        today=date.today()
        #day=today.strftime("%B %d,%Y")
        robot_brain=today.strftime("%B %d,%Y")
    elif "giờ" in you:
        now=datetime.now()
        #currentTime=now.strftime("%H giờ %M phút %S giây")
        robot_brain=now.strftime("%H %M phút %S giây")
    elif ("Tạm biêt" in you) or("tạm biệt" in you):
        robot_brain="Bye Duc Duy"
        print("Robot: " + robot_brain)
        # robot_mouth.say(robot_brain)
        # robot_mouth.runAndWait()
        # break
        output = gTTS(robot_brain, lang="vi", slow=False)
        x = "t" + str(i) + ".mp3"
        output.save(x)
        playsound.playsound(x, True)
        os.remove(x)
        break
    elif "mệt" in you:
        robot_brain="Anh nhớ giữ gìn sức khoẻ, giờ thì đi ngủ sớm đi"
        #tss=gTTS(text=robot_brain,Lang="vi")

    else:
        robot_brain="Tôi đang lắng nghe, xin bạn vui lòng nói lại "
    print("Robot: "+robot_brain)
    output = gTTS(robot_brain, lang="vi", slow=False)
    x = "t" + str(i) + ".mp3"
    output.save(x)
    playsound.playsound(x, True)
    os.remove(x)
    i = i + 1
    print("i",i)
    # robot_mouth.say(robot_brain)
    # robot_mouth.runAndWait()

    # tts=gTTS(text=robot_brain,lang='vi')
    # tts.save("pcvoice.mp3")
    # os.system("start pcvoice.mp3")
    # robot_mouth="robot_mouth"+str(i)+".mp3"
    # tts.save(robot_mouth)
    # playsound.playsound(robot_mouth)
    # i=i+1
    # print("i",i)