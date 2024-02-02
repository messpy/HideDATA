import binascii
import os
import pyautogui
import time

# パスワードファイルのパス
password_file_path = "password.txt"

# USBメモリ内のパスワードファイルを読み込む
with open(password_file_path, "rb") as f:
    password = f.read().decode("utf-8")

# パスワードを入力
pyautogui.write(password)
pyautogui.press("enter")

# サインイン画面が閉じるまで待つ
time.sleep(5)

# USBメモリ内のファイルを削除
os.remove(password_file_path)

# コンピュータを再起動
os.system("shutdown /r /t 0")
