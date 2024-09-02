import requests
from bs4 import BeautifulSoup
import re
import json

def get(url):
    page=requests.get(url)

    soup=BeautifulSoup(page.text,"html.parser")

    content=soup.find(class_="partial latest-stories")
    #print(tg)
    
    stories=[]
    for story in content.find_all(class_="latest-stories__item-headline"):
        title=story.text
        link1=content.find("a")
        link="https:/time.com"+link1.get("href")
        stories.append({"Title": title, "Link": link})
    return stories
url="https://time.com/"
stories=get(url)
json_data = json.dumps(stories, indent=2)
print(json_data)

    
