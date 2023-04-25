import time
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
import webbrowser
import os
import wikipedia
import pymongo
from mutagen.mp3 import MP3
import psutil
import pyjokes
import pyautogui
import json
import requests
from urllib.request import urlopen
import wolframalpha
s=pymongo.MongoClient('localhost',27017)
m=s.neural_schema




engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
print(voices)
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
wolframalpha_app_id = '[your]'

###########################################################
######################### to say ##########################
###########################################################

def speak(*audio):
    engine.say(audio)
    engine.runAndWait()

###########################################################
####################### to wish ###########################
###########################################################
    
def wishme():
    h=int(datetime.datetime.now().hour)
    if h>=0 and h<12:
        speak('good morning')
    elif h>=12 and h<18 :
        speak('good afternoon')
    else :
        speak('good night')

##############################################################
###################  to take voice input  ####################
##############################################################
        
def takecommand(recognizer, microphone):
    
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

        
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print("listning.....")
        audio = recognizer.listen(source)

    
    try:
        print("recognizing...")
        response= recognizer.recognize_google(audio )
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response


#################################################################
#############    to check weather he remembers   ###############
#################################################################
    
def know_yourself(y):
    x=m.people_info
    speak("say your name")
    print("say your name")
    cursor = x.find()
    n="yes"
    while("yes" in n):
        for d in cursor :
            print("what do you want to know about yourself")
            speak("what do you want to know about yourself")
            a=str(takecommand(recognizer,microphone)).upper()
            if d["NAME"]==y:
                print(d[a])
            print("do you want to know anything else")
            speak("do you want to know anything else")
            n=str(takecommand(recognizer,microphone)).upper()
            
#################################################################
#################  to find weather you exist ####################
#################################################################
            
def find_you(e):
    l=[]
    x=m.people_info
    cursor = x.find()
    n=0
    for d in cursor :
        l.append(d)
        if d["NAME"]==e:
            print(" you exist")
            speak("you exist in my memory "+ str(e))
            print("should i tell something about you ?")
            speak("should i tell something about you ")
            a=str(takecommand(recognizer,microphone)).lower()
            if "yes" in a:
                know_yourself()
            else:
                print("as your wish")
                speak("as your wish")
            
        else:
            n=n+1
    le=len(l)
    if n==le:
        print("you don't exist")
        print("please provide your details")
        people_info()


################################################################
################# to enter information of person ###############
################################################################
        
def people_info():
    x=m.people_info
    myrecord={}
    print("do you want to speak the information, or you want to write it yourself")
    speak("do you want to speak the information, or you want to write it yourself")
    ask=str(takecommand(recognizer, microphone)).lower()
    if "speak" in ask:
        print(' speak name : ')
        speak('speak name')
        a=str(takecommand(recognizer, microphone)).lower()
        print('name is ' ,a )
        print('is it right ?')
        speak('is it right ')
        w=str(takecommand(recognizer, microphone)).lower()
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            a=str(takecommand(recognizer, microphone)).lower()
            print('name is ' ,a )
            print('is it right ?')
            speak('is it right ')
            w=str(takecommand(recognizer, microphone)).lower()
        print('ok')
        myrecord['NAME']=a
        print(' speak age : ')
        speak('speak age')
        b=str(takecommand(recognizer, microphone)).lower()
        print('age is ' ,b )
        print('is it right ?')
        speak('is it right ')
        w=str(takecommand(recognizer, microphone)).lower()
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            b=str(takecommand(recognizer, microphone)).lower()
            print('age is ' ,b )
            print('is it right ?')
            speak('is it right ')
            w=str(takecommand(recognizer, microphone)).lower()
        print('ok')
        myrecord['AGE']=b
        print(' speak phone no. : ')
        speak('speak phone number')
        c=str(takecommand(recognizer, microphone)).lower()
        print('phone no. is ' ,c )
        print('is it right ?')
        speak('is it right ')
        w=str(takecommand(recognizer, microphone)).lower()
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            c=str(takecommand(recognizer, microphone)).lower()
            print('phone no. is ' ,c )
            print('is it right ?')
            speak('is it right ')
            w=str(takecommand(recognizer, microphone)).lower()
        print('ok')
        myrecord['PHONE_NO']=c
        print(' speak occupation : ')
        speak('speak name')
        d=str(takecommand(recognizer, microphone)).lower()
        print('occupation is ' ,d )
        print('is it right ?')
        speak('is it right ')
        w=str(takecommand(recognizer, microphone)).lower()
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            d=str(takecommand(recognizer, microphone)).lower()
            print('occupation is ' ,d )
            print('is it right ?')
            speak('is it right ')
            w=str(takecommand(recognizer, microphone)).lower()
        print('ok')
        myrecord['OCCUPATION']=d
        print(' speak relation : ')
        speak('speak relation')
        e=str(takecommand(recognizer, microphone)).lower()
        print('relation is ' ,e )
        print('is it right ?')
        speak('is it right ')
        w=str(takecommand(recognizer, microphone)).lower()
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            e=str(takecommand(recognizer, microphone)).lower()
            print('relation is ' ,e )
            print('is it right ?')
            speak('is it right ')
            w=str(takecommand(recognizer, microphone)).lower()
        print('ok')
        myrecord['RELATION']=e
        print(' speak address : ')
        speak('speak address')
        f=str(takecommand(recognizer, microphone)).lower()
        print('address is ' ,f )
        print('is it right ?')
        speak('is it right ')
        w=str(takecommand(recognizer, microphone)).lower()
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            f=str(takecommand(recognizer, microphone)).lower()
            print('address is ' ,f )
            print('is it right ?')
            speak('is it right ')
            w=str(takecommand(recognizer, microphone)).lower()
        print('ok')
        myrecord['ADDRESS']=f
        print("is their any other record")
        speak("is their any other record")
        s=str(takecommand(recognizer, microphone)).lower()
        while('yes' in s):
            record_id = x.insert(myrecord)
            print(record_id)
            people_info()
        record_id = x.insert(myrecord)
        print(record_id)
    elif 'write' in ask:    
        a=input("  name : ")
        print('name is ' ,a )
        print('is it right ?')
        speak('is it right ')
        w=input(" write yes or no")
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            a=input(" speak name : ")
            print('name is ' ,a )
            print('is it right ?')
            speak('is it right ')
            w=input("write yes or no")
        print('ok')
        myrecord['NAME']=a
        b=input("  age : ")
        print('age is ' ,b )
        print('is it right ?')
        speak('is it right ')
        w=input(" write yes or no")
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            b=input("  age : ")
            print('age is ' ,b )
            print('is it right ?')
            speak('is it right ')
            w=input(" write yes or no")
        print('ok')
        myrecord['AGE']=b
        c=input("  phone no. : ")
        print('phone no. is ' ,c )
        print('is it right ?')
        speak('is it right ')
        w=input(" write yes or no")
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            c=input("  phone no. : ")
            print('phone no. is ' ,c )
            print('is it right ?')
            speak('is it right ')
            w=input(" write yes or no")
        print('ok')
        myrecord['PHONE_NO']=c
        d=input("  occupation : ")
        print('occupation is ' ,d )
        print('is it right ?')
        speak('is it right ')
        w=input(" write yes or no")
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            d=input("  occupation : ")
            print('occupation is ' ,d )
            print('is it right ?')
            speak('is it right ')
            w=input(" write yes or no")
        print('ok')
        myrecord['OCCUPATION']=d
        e=input("  relation : ")
        print('relation is ' ,e )
        print('is it right ?')
        speak('is it right ')
        w=input(" write yes or no")
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            e=input("  relation : ")
            print('relation is ' ,e )
            print('is it right ?')
            speak('is it right ')
            w=input(" write yes or no")
        print('ok')
        myrecord['RELATION']=e
        f=input("  address : ")
        print('address is ' ,f )
        print('is it right ?')
        speak('is it right ')
        w=input(" write yes or no")
        while('no' in w):
            print('sorry for the misunderstanding from my side')
            print('please tell me again')
            f=input("  address : ")
            print('address is ' ,f )
            print('is it right ?')
            speak('is it right ')
            w=input(" write yes or no")
        print('ok')
        myrecord['ADDRESS']=f
        print("is their any other record")
        speak("is their any other record")
        s=str(takecommand(recognizer, microphone)).lower()
        while('yes' in s):
            record_id = x.insert(myrecord)
            print(record_id)
            people_info()
        record_id = x.insert(myrecord)
        print(record_id)


################################################################
############### to take question and answer ####################
################################################################


        
def question_answer():
    myrecord={}
    x=m.talking_schema
    speak("tell me your question")
    a=str(takecommand(recognizer, microphone)).lower()
    print('your question is ' ,a )
    print('is it right ?')
    w=str(takecommand(recognizer, microphone)).lower()
    if 'no' in w:
        speak('sorry for the misunderstanding from my side')
        print('please tell me again')
        speak('please tell me again')
        a=question_answer()
       
    else :
        print('ok')
        myrecord['user']=a
    n=1
    r='yes'
    while('yes' in r):
        speak("what is the answer")
        b=str(takecommand(recognizer, microphone)).lower()
        print("your answer is ", b)
        speak("your answer is ", b)
        speak("is it right ?")
        o=str(takecommand(recognizer, microphone)).lower()
        while('no' in o):
            speak('sorry for the misunderstanding from my side')
            print('please tell me again')
            speak('please tell me again')
            b=str(takecommand(recognizer, microphone)).lower()
            ans="answer"+str(n)
            myrecord[ans]=b
            o=str(takecommand(recognizer, microphone)).lower()
           
        print('ok')
        ans="answer"+str(n)
        myrecord[ans]=b
                
        print("is their any other answer")
        speak("is their any other answer")
        r=str(takecommand(recognizer, microphone)).lower()
        if "yes" in r:
            n=n+1
            
        
    print("is their any other question")
    speak("is their any other question")
    s=str(takecommand(recognizer, microphone)).lower()
    while('yes' in s):
        record_id = x.insert(myrecord)
        print(record_id)
        question_answer()
    else:
        record_id = x.insert(myrecord)
        print(record_id)

################################################################
#################### to give answer at random ##################
################################################################


def answer(w,e):
    import random
    x=m.talking_schema
    cursor = x.find()
    u=0
    l=[]
    
    n=0
    while(n>1):
        
        for d in cursor:
            l.append(d)
            if d["user"]==w:
                q=list(d)
                le=len(q)-2
                r=random.randint(1,le)
                t="answer"+str(r)
                print(d[t])
                gt=m.history
                history_dic={}
                history_dic['who']=e
                history_dic['what_asked']=w
                history_dic['date']=str(datetime.date.today())
                history_dic['time']=str(datetime.datetime.now().time())
                record_id_for_history_dic=gt.insert(history_dic)
                n=n+1
                
            elif d['user']!=w:
                 u=u+1
        if u==len(l)-1:
            print("no answer found")
            speak("no answer found")
            print("do you have any answer?")
            speak("do you have any answer")
            f=str(takecommand(recognizer, microphone)).lower()
            if "yes" in f:
                question_answer()
                 
            else :
                print("ok")
                speak("ok")
                break
            break
        break
#########################################################
######################to send email########################
##########################################################

    
def sendmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehol()
    server.starttls()
    server.login('your mail' , 'password')
    server.sendmail('your mail',to,content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent(interval=None))
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("Battery is at"+str(battery.percent))

def joke():
    speak(pyjokes.get_jokes())

def screenshot():
    img = pyautogui.screenshot()
    img.save("")





if __name__=='__main__':
    wishme()
    speak('My name is BEAST, I am Shawns personal assistance')
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("whats your name")
    speak("whats your name")
    e=str(takecommand(recognizer, microphone)).lower()
    if 'name' in e:
        print("Welcome Sir, How can I help you ?")
        speak("Welcome Sir, How can I help you")
    else:
        print(" Okay, How can I help You ? ")
        speak(" Okay, How can I help You ")
    
    while True:
        query=str(takecommand(recognizer, microphone)).lower()
        print("user said",query)
        if 'wikipedia' in query :
            speak('searching wikipedia . . ')
            query=query.replace('wikipedia' , '')
            result=wikipedia.summary(query , sentences = 2)
            speak('according to wikipedia')
            print(result)
            speak(result)
                                  
            
        elif 'open' in query :
            gt=m.history
            history_dic={}
            history_dic['who']=e
            history_dic['what_asked']=query
            history_dic['date']=str(datetime.date.today())
            history_dic['time']=str(datetime.datetime.now().time())
            record_id_for_history_dic=gt.insert(history_dic)
            print(record_id_for_history_dic)
            query=query.replace('open','')
            webbrowser.open(query+'.com')
            
        elif 'play' in query :
            query=query.replace('play','')
            #f2.write(query+' '+ str(datetime.datetime.now()))
            if 'music' in query :
                music_dir="path"
                music=os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, music[0]))
                
            elif 'song' in query :
                query=query.replace('song','')
                query=query+'.mp3'
                music_dir="path"
                music=os.listdir(music_dir)
                print(music)
                length=len(music)
                m=0
                for i in range(0,length-1):
                    if query==music[i]:
                        print(music[i])
                        audio=MP3("path/"+music[i])
                        s=audio.info.length
                        os.startfile(os.path.join(music_dir,music[i]))
                        time.sleep(s+5)
                    else:
                        m+=1
                        
                                            
                            
                if m==length:
                    speak('sorry not found in computer please search on youtube')
                    webbrowser.open('youtube.com')
                
            elif 'video' in query :
                gt=m.history
                history_dic={}
                history_dic['who']=e
                history_dic['what_asked']=query
                history_dic['date']=str(datetime.date.today())
                history_dic['time']=str(datetime.datetime.now().time())
                record_id_for_history_dic=gt.insert(history_dic)
                print(record_id_for_history_dic)
                query=query.replace('video')
                video_dir="E:\\"
                videos=os.listdir(video_dir)
                length=len(video)
                m=0
                for i in range(0,length-1):
                    if query==videos[i]:
                        print(videos[i])
                        audio=MP3("path/"+music[i])
                        s=audio.info.length
                        os.startfile(os.path.join(music_dir,music[i]))
                        time.sleep(s+5)
                    else:
                        m+=1
                
                                
                if m==length:
                    speak('sorry not found in computer please search on youtube')
                    webbrowser.open('youtube.com')
                        
        elif 'mail' in query:
            try:
                print("do you want to say or write yourself?")
                speak("do you want to say or write yourself")
                r=str(takecommand(recognizer, microphone)).lower()
                if 'write' in r:
                    speak("to whom")
                    to=input("please write here : ")
                    speak('what to say')
                    content=input("write here what you want to write")
                    sendmail(to,content)
                    speak('email has been sent')
                else:
                    speak("to whom")
                    to=takecommand(recognizer, microphone)
                    speak('what to say')
                    content=takecommand(recognizer, microphone)
                    content=content.replace('say that')
                    sendmail(to,content)
                    speak('email has been sent')
                    
            except Exception as e:
                print(e)
                speak("can't sent mail")
                
        elif 'show history_dic' in query:
            if 'wikipedia' in query:
                gt=m.wikipedia
                w=gt.find()
                for d in w:
                    print(d)
            else:
                gt=m.history
                e=gt.find()
                for d in e:
                    print(d)
        elif 'take one new question' in query:
            gt=m.history
            history_dic={}
            history_dic['who']=e
            history_dic['what_asked']=query
            history_dic['date']=str(datetime.date.today())
            history_dic['time']=str(datetime.datetime.now().time())
            record_id_for_history_dic=gt.insert(history_dic)
            
            question_answer()
        elif 'take a new record of a person' in query:
            gt=m.history
            history_dic={}
            history_dic['who']=e
            history_dic['what_asked']=query
            history_dic['date']=str(datetime.date.today())
            history_dic['time']=str(datetime.datetime.now().time())
            record_id_for_history_dic=gt.insert(history_dic)
            
            people_info()
            
        elif 'news' in query:
            print("which type of news you want to listen")
            speak("which type of news you want to listen")
            r=str(takecommand(recognizer, microphone)).lower()
            obj = requests.get('http://newsapi.org/v2/top-headlines?country=us&category='+r+'apiKey=[your]').json()
            i = 1
            data=obj
            print(data)
            speak("Following Are the Headlines.")
            for item in data["articles"]:
                print(str(i)+'.'+item["title"]+'\n')
                print(item["description"]+'\n')
                speak(item["title"])
                speak(item["description"])
                i += 1

        elif ('which is' in query) or ('what is' in query) or ('who is' in query) or ('how' in query) or ('where' in query):
            question = query
            print(" Which api you want to choose , Wolfram Alpha or Google")
            speak(" Which api you want to choose , Wolfram Alpha or Google")
            r=str(takecommand(recognizer, microphone)).lower()
            if 'wolfram alpha' in r:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.query(question)
                ans = next(res.results).text
                try:
                    print(ans)
                    speak(ans)
                except StopIteration:
                    print("No result Found")
                    speak("No result Found")
            else:
                query = query.replace("where is","")
                webbrowser.open_new_tab("https://www.google.com/"+query)


        elif 'cpu' in query:
            cpu()
            
        elif 'jokes' in query:
            joke()

        elif 'screenshot' in query:
            screenshot()

        elif 'log out' in query:
            os.system("shutdown -l")

        elif 'restart' in query:
            os.system("shutdown /r /t 1")

        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")

        elif 'Do not listening' in query:
            print("For How much time Sir?")
            speak("For How much time Sir?")
            r=int(takecommand(recognizer, microphone))
            print("Ok Sir, Going In Sleep Mode For ",r," seconds")
            speak("Ok Sir, Going In Sleep Mode For "+str(r)+" seconds")
            time.sleep(r)
        
        elif 'quit' in query:
           quit()

        elif query is not None:
            answer(query,e)
            speak('ok')
            
           
