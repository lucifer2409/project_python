import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as web
import os
import pywhatkit
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
      engine.say(audio)
      engine.runAndWait()

def wishme():
      hour = int(datetime.datetime.now().hour)
      if hour>=0 and hour<12:
            speak("Good morning abhishek !!")

      elif hour>=12 and hour<18:
            speak("Good afternoon abhishek")
      else:
            speak("Good evening")

      speak("I am zira sir how may i help you ")
def take_command():
      """
      It takes microphone input from the user
      """
      microphone = sr.Microphone()
      recognizer = sr.Recognizer()
      with microphone as source:
            print("Listening...")
            recognizer.pause_threshold = 1
            audio = recognizer.listen(source)

      try :
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print(f'user said :{query} \n')

      except Exception as e:
            print("Say that again please...")
            return "None"
      return query

if __name__ == "__main__":
      wishme()
      while True:
            query = take_command().lower()
      #Logic for executing task based on query
            if 'wikipedia' in query:
                  speak("Searching in wikipedia")
                  query = query.replace("Wikipedia","")
                  results = wikipedia.summary(query, sentences=2)
                  speak("According to wikipedia")
                  print(results)
                  speak(results)
            elif 'open youtube' in query:
                  web.open("youtube.com")

            elif 'open google' in query:
                  web.open("google.com")
            elif 'open github' in query:
                  web.open("github.com")
            elif 'playmusic' in query:
                  music_dir = ""
                  songs = os.listdir(music_dir)
                  print()
                  os.startfile(os.path.join(music_dir,songs[0]))


def youtubesearch(term):
      result ="https://www.youtube.com/results?search_query=" + term
      web.open(result)
      speak("This is what i found in the search result : ")
      pywhatkit.playonyt(term)
      speak("This may help you sir")

youtubesearch('carryminati')




