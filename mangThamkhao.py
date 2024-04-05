import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound
from datetime import date, datetime
i=0
r=sr.Recognizer()
while True:
    with sr.Microphone() as mic:
        audio =r.record(mic, duration=3)
        r.adjust_for_ambient_noise(mic)
        print("Tethys: ✿♥‿♥✿ ")
        audio =r.listen(mic)
        print("Tethys: ...")
    try:
        you = r.recognize_google(audio,language="vi")
    except:
        you = ""
        print("you: " + you)
    if you == "":
        robot_brain = "Bố còn đó không"
    elif "Xin chào" in you:
        robot_brain = "Chào bố Thế"
    #cảm súc
    elif "buồn" in you:
        robot_brain= "Bố có cần thời gian riêng tư không"
    #câu hỏi
    elif "tên bạn" in you:
        robot_brain= "À tên Tethys, được lấy ý tưởng từ nữ thần biển cả Tethys (Hy Lạp), một người vô cùng xinh đẹp "
    elif "người tạo ra" in you:
        robot_brain= you + " ư, là " +"Lê Văn Thế một người rất đẹp trai."
    elif "hôm nay" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "giờ" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H giờ %M phút")
    elif "tạm biệt" in you:
        robot_brain ="Tạm biệt bố"
        print("Tethys: " + robot_brain)
        output = gTTS(robot_brain,lang="vi", slow=False)
        x="t"+str(i)+".mp3"
        output.save(x)
        playsound.playsound(x, True)
        os.remove(x)
        break
    else :
        robot_brain= "Con chưa hiểu ý ạ "
    print("Tethys: " + robot_brain)
    output = gTTS(robot_brain,lang="vi", slow=False)
    x="t"+str(i)+".mp3"
    output.save(x)
    playsound.playsound(x, True)
    os.remove(x)
    i=i+1