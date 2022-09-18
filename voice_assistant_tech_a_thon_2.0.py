import pyttsx3
import datetime
import speech_recognition as sp
import webbrowser
import os
import googletrans
import pyjokes
import random
import requests
import math
import calendar
import instaloader
import winsound
import cowsay

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')  # getting details of current voice
# print(voices[1].id)#
engine.setProperty('voice', voices[1].id)  # setting voice male or fem


def speak(audio) :
    engine.say(audio)
    print(audio)
    engine.runAndWait()  # without this not able to listen the speech


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("Good Morning")

    elif (hour >= 12 and hour <= 17):
        speak("Good Afternoon")

    else:
        speak("Good Evening")
    speak("I am alexa Please tell me how may i help you!!!")

# def menu():
#  speak("I can:\nDo Calculations\nplay music\nTell:weather\njokes\nDate and Time\nOpen:\nRandom number game\nChrome\nyoutube\nWikipedia\nCode Editor\nGeeks For Geeks\nStack overflow\nCamera")

def takecommand():
    # it takes microphone input from user and returns string output#
    s = sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening...")
        s.energy_threshold = 800
        s.pause_threshold = 1
        audio = s.listen(source)

    try:
        print("Recognizing...")
        command = s.recognize_google(audio, language='en-in')  # Using google for voice recog#
        # if "alexa" in command:
        print("User said:", command)
    except:
        speak("Sorry unable to hear you!!")
        return "None"
    return command

def youtube():
    speak("Opening youtube....please wait")
    webbrowser.open("youtube.com")


def google():
    speak("Opening google...please wait!!")
    webbrowser.open("google.com")


def geeks():
    speak("Opening geeks....please wait!!")
    webbrowser.open("https://www.geeksforgeeks.org")

def music():
    music = "C:\\music"
    n = random.randint(0, 2)
    print(n)
    songs = os.listdir(music)  # it will provide list of musics in folder#
    print(songs)
    os.startfile(os.path.join(music, songs[n]))


def date_time():
    Time = datetime.datetime.now()
    speak("Current date and time is:")
    print(Time)


def code_editor():
    speak("Opening code editor....please wait!!")
    path = "C:\\Program Files\\CodeBlocks\\codeblocks.exe"
    os.startfile(path)


def jokes():
    speak("Please wait a moment")
    myjokes = pyjokes.get_joke(language='en', category=" all")
    translator = googletrans.Translator()
    translated = translator.translate(myjokes, dest="hindi")
    speak(translated.text)


# def camera():
#     speak("Opening camera...please wait!!")
#     path = "C:\Program Files (x86)\ManyCam\ManyCam.exe"
#     os.startfile(path)


def calculator():
    speak("Opening calculator....please wait!!")
    speak("Please make choice from given list:\n A.Arithmetic operation\n B.Conversion\n C.Trignometric function\n D.Others\n E.Exit ")

    while True:
        speak("Input Your choice---> ")
        choice = input()

        if choice == 'A':
            speak(" Select 1 for Addition\n Select 2 for Subtraction\n Select 3 for Multiplication\n Select 4 for True division\n Select 5 for Division\n Select 6 for Calculating powers")
            speak(" Enter Your choice: ")
            select = int(input())

            if (select == 1):

                speak("Input number 1:")
                n1 = int(input())
                speak("Input number 2:")
                n2 = int(input())
                speak("sum is")
                speak(n1 + n2)

            elif (select == 2):

                speak("Input number 1:")
                n1 = int(input())
                speak("Input number 2:")
                n2 = int(input())
                speak("subtraction is")
                speak(n1 - n2)

            elif (select == 3):

                speak("Input number 1:")
                n1 = int(input())
                speak("Input number 2:")
                n2 = int(input())
                speak("multiplication is")
                speak((n1 * n2))

            elif (select == 4):

                speak("Input number 1:")
                n1 = int(input())
                speak("Input number 2:")
                n2 = int(input())
                speak("True division is")
                speak(n1 / n2)

            elif (select == 5):

                speak("Input number 1:")
                n1 = int(input())
                speak("Input number 2:")
                n2 = int(input())
                speak("Division is")
                speak(n1 // n2)

            elif (select == 6):

                speak("Input number 1:")
                n1 = int(input())
                speak("Input number 2:")
                n2 = int(input())
                speak("Power is")
                speak(n1 ** n2)

            else:
                speak("Invalid choice")

        elif choice == 'B':

            speak(" Select 1 for Decimal to Binary\n Select 2 for Decimal to Octal\n Select 3 for Decimal to Hexadecimal")
            speak(" Enter Your choice--->> ")
            select = int(input())

            if (select == 1):
                speak("Input a number")
                num = int(input())
                speak(bin(num))

            elif (select == 2):
                speak("Input a number")
                num = int(input())
                speak(oct(num))

            elif (select == 3):
                speak("Input a number")
                num = int(input())
                speak(hex(num))


        elif choice == 'C':

            speak(" Select 1 for Sin\n Select 2 for Cos\n Select 3 for Tan\n Select 4 for Log")
            speak(" Enter Your choice: ")
            select = int(input())

            if (select == 1):
                speak("Input a number")
                num = int(input())
                speak(math.sin(num))

            if (select == 2):
                speak("Input a number")
                num = int(input())
                speak(math.cos(num))

            if (select == 3):
                speak("Input a number")
                num = int(input())
                speak(math.tan(num))

            if (select == 4):
                speak("Input a number")
                num = int(input())
                speak("Input a base: ")
                base = int(input())
                speak(math.log(num))

        elif choice == 'D':

            speak(" Select 1 for Factorial\n Select 2 for GCD\n Select 3 for LCM\nSelect 4 for Square root")
            speak(" Enter Your choice-->>")
            select = int(input())

            if select == 1:
                speak("Input a number: ")
                num = int(input())
                speak(math.factorial(num))

            elif select == 2:
                speak("Input number 1: ")
                num1 = int(input())
                speak("Input number 2: ")
                num2 = int(input())
                speak(math.gcd(num1, num2))

            elif select == 3:
                speak("Input number 1: ")
                num1 = int(input())
                speak("Input number 2: ")
                num2 = int(input())
                speak(math.lcm(num1, num2))

            if select == 4:
                speak("Input a number: ")
                num = int(input())
                speak(math.sqrt(num))

        elif (choice == 'E'):
            break


def calendar():

    import calendar
    speak("Input Year:")
    year=int(input())
    speak("Input month")
    mm = int(input())
    speak("Caledar is:")
    print(calendar.month(year, mm))


def instagram_dp():
    try:
        speak("Downloading instagram Dp...please wait a moment!!")
        j = instaloader.Instaloader()
        speak("Enter username:")
        profile = input()
        j.download_profile(profile, profile_pic=True)

    except:
        speak("Downloaded!!")

def beep():

    frequency = 3300  # The frequency must be in the range 37 through 32,767 hertz.
    duration = 7000  # 1000ms=1sec
    winsound.Beep(frequency, duration)

def animal():
    l1 = {}
    l1 = cowsay.char_names
    y = random.randint(1, 15)
    i = 0
    for k in l1:
        i = i + 1
        if (y == i):
            speak("Displaying "+k)
            print(cowsay.get_output_string(k, "*"))

def stone_paper_scissor():
     while(True):
         speak("Enter your choice-->")
         speak("1 for stone\n2 for scissor\n3 for paper\n4 for exit")
         i = int(input())
         if (i == 1):
             speak("user choose:stone")
         elif (i == 2):
             speak("user choose:scissor")
         elif (i == 3):
             print("user choose:paper")
         if (i != 4):
             n = random.randint(1, 3)
             if (n == 1):
                 speak("computer choose:stone")
             elif (n == 2):
                 speak("computer choose:scissor")
             elif (n == 3):
                 speak("computer choose:paper")
             if (i == n):
                 speak("Draw")
             elif (i == 1 and n == 2 or i == 2 and n == 3 or i == 3 and n == 1):
                 speak("win")
             elif (i == 1 and n == 3 or i == 3 and n == 2 or i == 2 and n == 1):
                 speak("lose")
         elif (i == 4):
             exit()


if __name__ == "__main__":
    speak('Hii')
    wishMe()
    # menu()

    while (True):
        command = takecommand().lower()

        if "alexa" in command:

            if "youtube" in command:
                youtube()

            elif "google" in command:
                google()

            elif "play music" in command:
                music()

            elif "code editor" in command:
                code_editor()

            elif "date and time" in command:
                date_time()

            elif "joke" in command:
                jokes()
            # elif "camera" in command:
            #     camera()

            elif "geeks" in command:
                geeks()

            elif "hai" in command:
                speak("Hello")

            elif "how are you" in command:
                speak("I am good!!")

            elif "are you single" in command:
                speak("I am in relationship with wifi")

            elif "it's too cold" in command:
                speak("Hello friends chai peelo")

            elif "date" in command:
                speak("Sorry i have a headache")

            elif "calculator" in command:
                calculator()

            elif "calendar" in command:
                calendar()

            elif "download instagram dp" in command:
                instagram_dp()

            elif "beep sound" in command:
                beep()

            elif "shut down" in command:
                speak("Shutting down please wait a moment..")
                os.system("shutdown /h")

            elif "animal sketch" in command:
                animal()

            elif "paper" in command:
                stone_paper_scissor()

            elif "stop" in command:
                exit()

        else:
            speak("Say command again!")
        input()
