import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyaudio
import smtplib
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


def sendEmail(to, content):
      server = smtplib.SMTP('smtp.gmail.com',587)
      server.ehlo()
      server.starttls()
      server.login('trivedi.a@gmail.com')
      server.sendmail('youremail@gmail.com' , 'your-password')
      server.close()


if __name__ == "__main__":
      wishme()
      while 1:
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
                  webbrowser.open("youtube.com")

            elif 'open google' in query:
                  webbrowser.open("google.com")
            elif 'open github' in query:
                  webbrowser.open("github.com")
            elif 'playmusic' in query:
                  music_dir = ""
                  songs = os.listdir(music_dir)
                  print()
                  os.startfile(os.path.join(music_dir,songs[0]))
            elif 'the time' in query:
                  strTime = datetime.datetime.now().strftime("%H:%H:%S")
                  speak(f"Sir , the time is {strTime}")
                  print(strTime)
            elif 'open code' in query:
                  code_path = "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                  os.startfile(code_path)
            elif 'email to abhishek' in query:
                  try:
                        speak("What should I say ?")
                        content = take_command()
                        to = "trivedi.a@somaiya.edu"
                        sendEmail(to,content)
                        speak('Email has been sent!')
                  except Exception as e:
                        print(e)
                        print("Sorry abhishek i cannot send the following mail !")


