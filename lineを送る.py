import requests
import tkinter as tk
from tkinter import messagebox
import tkinter.ttk as ttk





def line(me):
    url = "https://notify-api.line.me/api/notify" 
    token = "mmjcR1plHjBEGizK6p3ZP7rA9hERqz9VwDhfNr1VOKf"
    headers = {"Authorization" : "Bearer "+ token} 
    message =  me
    payload = {"message" :  message} 
    r = requests.post(url, headers = headers, params=payload)
    
x = input("内容を入力してください")

line(x)


