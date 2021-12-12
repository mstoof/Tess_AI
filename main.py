import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import smtplib

def assistant(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        assistant("Hello,Good Morning")
        print("Hello,Good Morning")
    elif hour >= 12 and hour < 18:
        assistant("Hello,Good Afternoon")
        print("Hello,Good Afternoon")
    else:
        assistant("Hello,Good Evening")
        print("Hello,Good Evening")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            assistant("Pardon me, please say that again")
            return "None"
        return statement

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()



if __name__ == '__main__':
    print("Loading your AI personal assistant G-One")
    wishMe()
    assistant('I am Tess, your AI assistant. Please tell me how may I help you')

    while True:
        query = takeCommand().lower()
        print(query)
        # Logic for executing tasks based on query

        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            assistant('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5) 
            assistant("According to Wikipedia")
            print(results)
            assistant(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            assistant("Google Mail open now")
            time.sleep(5)

        elif 'email to' in query:
            try:
                assistant("What should I say?")
                content = takeCommand()
                to = "receiver's email id"
                sendEmail(to, content)
                assistant("Email has been sent!")
            except Exception as e:
                print(e)
                assistant("Sorry sir. I am not able to send this email")

        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            assistant('Here are some headlines from the Times of India,Happy reading')
            time.sleep(6)

        elif 'search'  in query:
            statement = query.replace("search", "")
            webbrowser.open_new_tab(statement)
            time.sleep(5)

        elif 'play music' in query:
            music_dir = 'music_dir_of_the_user'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            assistant(f"The time is {strTime}")

        elif 'open stack overflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'ask' in query:
            assistant('I can answer to computational and geographical questions  and what question do you want to ask now')
            question=takeCommand()
            app_id=os.getenv('WOLFRAM_API')
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            assistant(answer)
            print(answer)

        elif 'who are you' in statement or 'what can you do' in statement:
            assistant('I am Tess version 1 point O your personal assistant. I am programmed to minor tasks like'
                  'opening youtube,google chrome, gmail and stackoverflow ,predict time,take a photo,search wikipedia,predict weather'
                  'In different cities, get top headline news from times of india and you can ask me computational or geographical questions too!')


        elif "who made you" in statement or "who created you" in statement or "who discovered you" in statement:
            assistant("I was built by Maurice")
            print("I was built by Maurice")

        elif "weather" in statement:
            api_key=os.getenv('OPENWM')
            base_url="https://api.openweathermap.org/data/2.5/weather?"
            assistant("what is the city name")
            city_name=takeCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                assistant(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

        elif "log off" in statement or "sign out" in statement:
            assistant("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])





        
            
