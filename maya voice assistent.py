import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener =sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')  #to convert a voice male to female. 
engine.setProperty('voice',voices[1].id)
#engine.say('i am your alexaa')
#engine.say('what can i do for you')

def talk (text):  # talk function user commands are convert to text to talk.
     engine.say(text)
     engine.runAndWait()


def take_command():
        try:
                    with sr.Microphone() as source:
                        print('listening....')
                        voice=listener.listen(source)
                        command=listener.recognize_google(voice)
                        command=command.lower()
                        if 'maya' in command:
                            command=command.replace('maya', '')
                            print(command)
                            # talk(command)
        except:
            pass    
        return command

   
def run_maya():
      command = take_command()
      print(command)
      if  'play' in command:
          song =command.replace('play', '')
          talk('playing' + song)
          #print('playing')
          pywhatkit.playonyt(song)
      elif  'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            #print(time)
            talk('Current time is '+ time)
      elif 'who the heck is ' in command:
            person =command.replace('wh the heck is ', '')
            info =wikipedia.summary(person,1)
            print(info)
            talk(info)
      elif 'joke' in command:
            talk(pyjokes.get_joke())
      else:
            talk('please say the command again.')
while True:
    run_maya()