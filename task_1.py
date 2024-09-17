import speech_recognition as sr # type: ignore
import webbrowser
import pyttsx3 # type: ignore
import music_library
import google.generativeai as genai

# Initialize recognizer
recognizer = sr.Recognizer()  # Correct capitalization

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait() 
    
def aiprocess(text):
    # Configure the API key
    genai.configure(api_key="AIzaSyDNXHHkaVoP96gRVGYr65TRJ2wbQh0KSu0")
    # create your api key and use it
    
    # Generate a response based on the input text
    response = genai.generate_text(
        prompt=text,
        model="models/text-bison-001",  # Example model
        temperature=0.7,  # Control creativity
        max_output_tokens=60  # Limit the length of the response
    )
    
    # Extract the generated text from the response
    short_answer = response.result
    
    return short_answer

    
    
def process_command(text):
    print("positive") 
    # print(text)
    
    if "open google" in  text.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in text.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in text.lower():
        webbrowser.open("https://youtube.com")
    elif "open instagram " in text.lower():
        webbrowser.open("https://instagram.com")
    elif "open internship" in text.lower():
        webbrowser.open("https://www.oasisinfobyte.com/")
        
    elif text.lower().startswith("play"):
        song1=text.lower().split(" ")[1] #text=['play','coke',studeo] by giving this operation s1='cke'and s2='std'
        song2=text.lower().split(" ")[2]#split func seperate all elements and stores in list
        link=music_library.music[song1+" "+song2]
        webbrowser.open(link)
        
    else:
        #let gemini  handle request
        output=aiprocess(text)
        print(output)
        speak(output)
        
        
    
if __name__ == "__main__":
    speak("Hello sir, Jarvis is here.....")
    speak("how can I help you ?")
    
    # listen when any one is speaking jarvis
    # speak from ur microscope
    
    while True :
        r=sr.Recognizer()
        print("recognizing...")
        speak("before asking anything prompt JARVIS ")
        try:
            with sr.Microphone() as source:
                print("listening........")
                audio = r.listen(source, timeout=10,phrase_time_limit=5)# listen function from sr takes two parameters (command,timeout)
                # Recognize speech using Google Web Speech API (default)
            word = r.recognize_google(audio)
            
            # speak("You said: " + word)
            # speak("before asking anything prompt JARVIS ")
            
            if (word.lower() == "jarvis"): #condition for jarvis matches then response is given
                speak("yes sir")
                
                with sr.Microphone() as source:
                    print("jarvis empowered.....")
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    speak("You said: " + text)
                    # if text:
                    process_command(text)

        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            speak("Sorry, I couldn't understand that.")             
                
        except sr.RequestError:
            print("Could not request results from the speech recognition service.")
            speak("I'm having trouble connecting to the recognition service.")
    
