import os
import speech_recognition as sr
from gtts import gTTS

from phue import Bridge
import random

bridge = Bridge("192.168.1.90")

bridge.connect()

bridge.get_api()

bridge.set_light([1, 2], 'on', True) # Change to False to switch off the light

def get_Audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
            print("Input")
            print(said)
        except Exception as e:
            bridge.set_light(1, "hue", random.randrange(0, 65535))
            bridge.set_light(2, "hue", random.randrange(0, 65535))
            # print(f"Eception: {str(e)}")



while True:
    get_Audio()