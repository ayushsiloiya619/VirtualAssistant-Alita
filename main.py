import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import requests
import pywhatkit
import pyjokes

# Set up OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    elif 21 <= hour < 22:
        speak("Sir i think we should pack up with our work.  Time to go for the dinner!")

    elif 24 <= hour:
        speak("Time to fly in a dreams. Goodnight sir!!")


    else:
        speak("Good Evening!")

    speak("I am alita sir your personal assistant . Please tell me how can i help you today ? ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Ayush sir i am listening to you speak...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Fetching the information please be patient...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        print("Oops! sorry i didn't catch your voice...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open blogger' in query:
            webbrowser.open("https://www.blogger.com/blog/posts/8732388446713754997?hl=en-GB&tab=jj")


        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'play' in query:
            song = query.replace("play", "")
            speak("Playing" + song)
            pywhatkit.playonyt(song)

        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "thank you" in query:
            speak("It's my pleasure sir.")

        elif "beautiful" in query:
            speak("Aww thank you sir.")
        elif "good" in query:
            speak("Thank you sir."
                  "Is their anything else you want to know sir.")

            # elif "no" in query:
            speak("OK!")

        elif "weather" in query:
            API_KEY = ""
            BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

            city = "kanpur"
            requests_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

            response = requests.get(requests_url)

            if response.status_code == 200:
                data = response.json()
                weather = data["weather"][0]["description"]
                temperature = round(data["main"]["temp"] - 273.15, 2)
                t = temperature
                w = weather
                speak(f"Sir today the weather is:{w}")
                speak(f"& Sir the temperature is:{t}degree celsius")

            else:
                speak("error occurred ")

        elif "not yet" in query:
            speak(
                "Okay sir , ur wish!  Might your mom will be coming near to you and wrap up you in a plate. Didn't "
                "you try!")

            # elif "ok" in query:
            speak("OK!")

        elif "love you" in query:
            speak('aww Love you too sir!')

        elif "name" in query:
            speak("My name is Alita! Programmed by Ayush Siloiya")

        elif 'motivation' in query:
            speak("The man who does not read books has no advantage over the one who cannot read them. \
                The beautiful thing about learning is that no one can take it away from you.")
        
        elif 'help' in query:
                response = openai.Completion.create(
                engine="davinci-codex",
                prompt=prompt,
                temperature=0.5,
                max_tokens=200,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0
            )
            brief = response.choices[0].text.strip()
            speak(brief)
            print(brief)
