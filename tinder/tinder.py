import cv2
import pyautogui
import numpy as np
import time
import random
import logging
import json
import requests

def setup_logging(log_file):
    """ログの設定を行う関数"""
    logging.basicConfig(filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')
    print("関数をファイル名を指定して呼び出してください「logging.info()」")


def get_json(key=""):
    filename = "data.json"
    with open(filename, 'r') as file:
        data = json.load(file)
        if key in data:
            return data[key]
        else:
            print(f"Error: Key '{key}' not found in JSON file.")
            return None


def send_line(token,msg):
        print("LINEに送信中")
        url = "https://notify-api.line.me/api/notify"
        headers = {"Authorization" : "Bearer "+ token}
        payload = {"message" :  msg}
        r = requests.post(url, headers = headers, params=payload)



def click_image(image_path, threshold=0.9):
    # 画像を読み込む
    screen = pyautogui.screenshot()
    screen_np = cv2.cvtColor(np.array(screen), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path)

    # テンプレートマッチングを行う
    result = cv2.matchTemplate(screen_np, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 類似度がしきい値以上の場合、画像の中心座標をクリック
    if max_val >= threshold:
        w, h = template.shape[:-1]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        pyautogui.click(center_x, center_y)
        print("画像が見つかりました。クリックしました。")
        return 1
    else:
        print("画像が見つかりませんでした。")
        return 0


def ocr(flename='read_ocr.png'):
    import pyautogui
    import pytesseract
    from PIL import ImageGrab
    
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program files\Tesseract-OCR\tesseract.exe'
        
        pyautogui.screenshot(flename, region=(689,458,510,150)) 
        #pyautogui.screenshot(flename)
        print(flename)
        time.sleep(3)
        print("OCR検出中")
        #OCRを実行して文字を検出
        text = pytesseract.image_to_string(flename)
        # 検出された文字列を表示
        print("検出された文字列:")
        print(text)

    except Exception as e:
        print(f"エラー: {e}")
        text = ""
    return text
setup_logging("tinder.log")
jsond = get_json("line")
i = 1
while True:
    # メイン関数
    i += 1
    txt = ocr("data.png")
    txt = txt + str(i)+"回目"
    findpht = click_image('good.png')
    print(txt)
    logging.info(txt)
    if findpht == 0:
        findpht = click_image('good2.png')
        if findpht == 0:
            findpht = click_image('batu.png')
            if findpht == 0:
                findpht = click_image('baatu.png')
                if findpht == 0:
                    findpht = click_image('kekko.png')

    t = random.uniform(0,10)
    print(t)
    time.sleep(t)
