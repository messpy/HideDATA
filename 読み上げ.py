import  pyttsx3

    #print(dsk.percent,"%")

for e in range(100):
    text = input("入力")
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
