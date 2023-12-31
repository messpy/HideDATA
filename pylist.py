       
import glob
import os
import PySimpleGUI as sg


ff = r"C:\Users\kent\Desktop\PythonF\*.py*"
fld = glob.glob(ff)
fld.sort()
data=[]
for i,f in enumerate(fld):
    x = os.path.basename(os.path.dirname(f))
    y = os.path.splitext(os.path.basename(f))[0]
    data.append(y)
    print(i,y)
print("\n")
#n = int(input("種目:"))
#n = data[n]





layout = [
            [sg.MenuBar([['ファイル',['新規ファイル','---','終了']]], key='menu1')],
            [sg.Text("お帰りなさい")],
            [sg.Listbox(data, size=(30, len(data)),key='list'),sg.Button('OK')]
            ]

window = sg.Window("title",layout)

while True:
    event,value=window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "OK":
        if value["list"]:
            sg.popup(value["list"][0])
            __import__("PythonF." + value["list"][0])

window.close


"""


for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    __import__(module[:-3], locals(), globals())
del module

"""
