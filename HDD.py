import psutil 
import time
import  pyttsx3

    #print(dsk.percent,"%")

engine = pyttsx3.init()

print("hi")
engine.say("hello")
engine.runAndWait()


i = 0
g = 0
while True:
    dsk = psutil.disk_usage('/')

    btr1 = psutil.sensors_battery()
    time.sleep(60)
    i += 1

    print(i)
    btr2 = psutil.sensors_battery()
    if btr1 != btr2:
        g +=1
        print(str(i),":",str(g),":",str(btr2.percent) + "%")
        engine.say(str(btr2.percent) + "%")
        engine.runAndWait()
        
