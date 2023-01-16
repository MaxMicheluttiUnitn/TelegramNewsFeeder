
import datetime
from typing import List
import requests
from src.classes.user import User
from dotenv import load_dotenv
from src.classes.news import Feed
import os

from src.methods.sendMessage import sendMessage
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL")
API_PASWORD = os.getenv("API_PASSWORD")
NEWS_API_URL = os.getenv("NEWS_API_URL")
NEWS_API_TOKEN = os.getenv("NEWS_API_KEY")

def get_news(token: str):
    users: List[User] = getUsers(token)
    news: Feed = retrieve_news()
    print(users)
    print(news)
    for user in users:
        for new in news["articles"]:
            message=f'''{new["title"]}
{new["url"]}'''
            sendMessage(chat_id=user["chat_id"],return_msg=message)

def getUsers(token: str):
    result = requests.get(API_URL+'/users', headers={"token": token})
    users: List[User] = result.json()
    return users

def retrieve_news():
    last_hour_date_time = datetime.datetime.now() - datetime.timedelta(hours = 1)
    from_str=last_hour_date_time.isoformat()
    to_str=datetime.datetime.now().isoformat()
    result = requests.get(NEWS_API_URL+f"/everything?q=Pallavolo Femminile&from={from_str}&to={to_str}",
    headers={
        "Authorization": NEWS_API_TOKEN
    })
    news:Feed = result.json()
    return news