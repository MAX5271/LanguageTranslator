from gtts import gTTS
import pygame
import time


def speak(text: str, language: str) -> None:
    speech = gTTS(text=text, lang=language, slow=False)
    speech.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3") 
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    
