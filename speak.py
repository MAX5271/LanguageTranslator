from gtts import gTTS
import pygame
import time
#importing the required dependences and api(s)

#function for text to speech
def speak(text: str, language: str) -> None:
    speech = gTTS(text=text, lang=language, slow=False)#using google text to speeck to create an audio save file
    speech.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3") #playing the audio text to speech
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # wait for music to finish playing
        time.sleep(1)
    
