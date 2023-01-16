import datetime
import threading
import time
from src.methods.get_news import get_news
import schedule
import requests
from dotenv import load_dotenv
import os
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")


token=""

def main():
    print("starting...")
    getToken()
    # refreshing token twice a day
    schedule.every().day.at("00:00").do(refreshToken)
    schedule.every().day.at("12:00").do(refreshToken)

    for i in range(10,24):
        schedule.every().day.at(str(i)+":49").do(get_news, token)
    
    print("loading done...")
    
    try:
        while(True):
            time.sleep(10)
            schedule.run_pending()
    finally:
        print("ending...")

def refreshToken():
    thread=threading.Thread(getToken)
    thread.start()

def getToken():
    content={'password':API_PASWORD}
    res=requests.post(url=API_URL+'/login',json=content)
    response = res.json()
    global token 
    token =  response['token']

if __name__=="__main__":
    main()