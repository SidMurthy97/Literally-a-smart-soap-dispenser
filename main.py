from gtts import gTTS
import os 
from bs4 import BeautifulSoup as soup
import requests
import random

def text_to_speech(fact):
    
    fact = "Hello! Did you know? " + fact + "Thanks for listening, have a great day!"
    
    language = 'en' 

    tts = gTTS(text=fact,lang=language)

    tts.save("fact.mp3")
    os.system("mpg321 fact.mp3")

def get_fact():
    fact_length = 0
    
    page = requests.get("https://www.thefactsite.com/1000-interesting-facts/")
    Soup = soup(page.content, 'html.parser')

    while fact_length < 150:
        random_index = random.randint(7,116)
        fact = Soup.find_all('p')[random_index].get_text()
        fact_length = len(fact)

    print(fact)
    return fact

if __name__ == '__main__':
    

    fact = get_fact()
    text_to_speech(fact)
