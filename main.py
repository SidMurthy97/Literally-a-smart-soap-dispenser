from gtts import gTTS
import os 
from bs4 import BeautifulSoup as soup
import requests

def text_to_speech():
    test_text = 'Hi, this is Anakin Skywalker and I want to let you know, Dishita Murthy, that you suck at Zelda'
    language = 'en' 

    tts = gTTS(text=test_text,lang=language)

    tts.save("test.mp3")
    os.system("test.mp3")


if __name__ == '__main__':
    
    page = requests.get("https://www.thefactsite.com/1000-interesting-facts/")
    Soup = soup(page.content, 'html.parser')
    print(len(Soup.find_all('p')))
    
    for i in range(len(Soup.find_all('p'))):
        print(i, Soup.find_all('p')[i].get_text())
    
    #print(soup.prettify())