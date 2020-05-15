from gtts import gTTS
import os 
from bs4 import BeautifulSoup as soup
import requests
import random
import RPi.GPIO as GPIO
import time
import pygame

#setup object

#GPIO/servo
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo = GPIO.PWM(11,50)

#TTS/pygame
language = 'en'
pygame.mixer.init()

#web scrape
page = requests.get("https://www.thefactsite.com/1000-interesting-facts/")
Soup = soup(page.content, 'html.parser')

def text_to_speech(fact):
    
    fact = "Hello! Did you know? " + fact + "Thanks for listening, have a great day!"
    tts = gTTS(text=fact,lang=language)
    tts.save("fact.mp3")
    pygame.mixer.music.load("fact.mp3")
    

def get_fact():
    fact_length = 0
    while fact_length < 150:
        random_index = random.randint(7,116)
        fact = Soup.find_all('p')[random_index].get_text()
        fact_length = len(fact)

    print(fact)
    return fact
def run_servo(servo):
    
    servo.start(0)
    duty = 2

    while duty <= 12:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.03)
        duty = duty + 0.5
    while duty >= 2:
        servo.ChangeDutyCycle(duty)
        time.sleep(0.03)
        duty = duty - 0.5
    
    servo.stop()


if __name__ == '__main__':
    
    fact = get_fact()
    text_to_speech(fact)
    
    for i in range(5):
        print(i)
        x = input("enter number")
        
        if x == '1':
            pygame.mixer.music.play()
            run_servo(servo)
            
            while pygame.mixer.music.get_busy() == True:
                continue
            #load next fact 
            fact = get_fact()
            text_to_speech(fact)
            

