from email.mime.text import MIMEText
import smtplib
 
# SMTP認証情報
account = "sekaionch"
password = ""
 
# 送受信先
to_email = ""
from_email = "
 
# MIMEの作成
subject = "Pythonのテストメール"
mes = input("本文の入力：")
message = mes
msg = MIMEText(message, "html")
msg["Subject"] = subject
msg["To"] = to_email
msg["From"] = from_email
 
# メール送信処理
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(account, password)
server.send_message(msg)
server.quit()


print(from_email)
print("送信しました")
