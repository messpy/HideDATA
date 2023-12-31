import glob
import os
import shutil
files = glob.glob("*.*")

for f in files:
    desk = r"C:\Users\kent\Desktop"
    fk = os.path.splitext(f)[1][1:]

    print(fk)
    dk = desk + "\\" + fk
    print(dk)
    k = os.path.isdir(dk)
    if k == False:
        os.mkdir(dk)
    else:
        pass

    shutil.move(f,dk)
