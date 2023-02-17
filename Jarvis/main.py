import speech_recognition as sr
import webbrowser
import requests
from bs4 import BeautifulSoup
from speech_recognition import AudioData


def search_google(query):
    """Searches for a query on Google"""
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)


def get_weather(location):
    """Gets the current weather for a location"""
    url = f"https://www.google.com/search?q={location}+weather"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    temperature = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).text
    condition = soup.find("div", attrs={"class": "BNeawe tAd8D AP7Wnd"}).text
    print(f"Current temperature in {location} is {temperature} and the weather condition is {condition}")


def open_website(url):
    """Opens a website in a web browser"""
    webbrowser.open(url)


# Initialize the speech recognizer
# Main function


while True:
    # Record audio from the microphone
    microphone = sr.Microphone()
    recognizer = sr.Recognizer()
    with microphone as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    # Process the user's speech
    try:
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")

        # Process the command
        if "search" in command:
            query = command.split("search", 1)[1].strip()
            search_google(query)
        elif "weather" in command:
            location = command.split("weather", 1)[1].strip()
            get_weather(location)
        elif "open" in command:
            url = command.split("open", 1)[1].strip()
            open_website(url)
        elif "exit" in command:
            break
        else:
            print("Invalid command. Please try again.")
    except sr.UnknownValueError:
        print("Sorry, I didn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")