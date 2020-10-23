import pyttsx3 # importing module
import datetime
import speech_recognition as sr #speech regonition module
import wikipedia 
import smtplib #for sending email
import webbrowser as wb
import pyautogui #for taking screenshot
import psutil  #for cpu and battery status 
import pyjokes 

engine = pyttsx3.init()

def speak(audio):     #Text to Speak function
    engine.say(audio)
    engine.runAndWait()

#Changing voice of assistant and set speed rate
voice = engine.getProperty('voices') #Getting the voice property
engine.setProperty('voices',voices[0].id)  #setting voice
newVoiceRate = 150
engine.setProperty('rate',newVoiceRate)


def time():        #Time Function
    time=datetime.datetime.now().strftime("%H:%M:%S")
    speak(time)


def date():
    year=int(dtaetime.datetime.now().year)
    month=int(dtaetime.datetime.now().month)
    date=int(dtaetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def wishme():                #Greet us function
    speak("Welcome Back Sir")
    hour = datetime.datetime.now().hour

    if hour>=6 and hour<12:
        speak("good morning")
    elif  hour>=12 and hour<18:
        speak("good afternoon")
    elif  hour>=18 and hour<=24:
        speak("good evening")
    else
        speak("good night")


def takeCommand():             #Taking Command using microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,'en=US')
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please")
         return "None"

    return query


def sendmail(to,content) :       #sending email function
    server=smtplib.SMIP('smtp.gmail.com',587)
    server.ehlo()
    server,startls()
    server.login("test@gmail.com","123test")
    server.sendmail("test@gmail.com",to,content)
    sever.close()


def screenshot():            #Taking screenshot function
    img = pyautogui.screenshot()
    img.save("E:\sahbaz\ss.png")


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at "+ usage)
    battery = psutil.sensors_battery
    speak("Battery is at")
    speak(battery.percent)


def jokes():
    speak(pyjokes.get_joke())


if __name__ =="__main__":

    wishme()

    while True:
        query = takeCommand().lower()
        print(query)

        if "time"  in query:
            time()
        elif "date" in query:
            date()
        elif "offline" in query:
            quit()
        elif "wikipedia" in query:
            speak("Searching....")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            speak(result)
        elif  "send email" in query:
            try:
                speak("What should i say")
                content=takeCommand()
                to="xyx@gmail.com"
                sendmail(to,content)
                speak(content)
            except Exception as e:
                speak(e)
                speak("Unable to send the message")
        elif "Search in chrome" in query:
            speak("What should i search")
            chromepath = "C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
            search=takeCommand().lower()
            wb.get(Chromepath).open_new_tab(search+".com")
        elif "logout" in query:
            os.system("shutdown - l")
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
        elif "restart" in query:
            os.system("shutdown /r /t l")
        elif "play song" in query:
            songs_dir="F:\music\music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))
        elif "remember that" in query:
            speak("What should i remember ")
            data = takeCommand()
            speak("You said me to remember"+ data)
            remember = open("data.txt","w")
            remember.write(data)
            remember.close()

        elif "Do you know anything" in query:
            remember = open("data.txt","r")
            speak("You said me to remember that" + remember.read())
        elif "Screenshot" in query:
            screenshot()
            speak("Done")
        elif "cpu" in query:
            cpu()
        elif "joke" in query:
            jokes()
#END

