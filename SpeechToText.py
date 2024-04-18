import speech_recognition as sr
#pip install pygobject
#pip install preferredsoundplayer
#from preferredsoundplayer import playsound
#pip install PyObjC
#from pydub import AudioSegment
#pip install playsound
#pip install gtts
#pip install SpeechRecognition pydub

filename = "male.wav"

# Initialize the recognizer
r = sr.Recognizer()

# Open the file
with sr.AudioFile(filename) as source:
    # Listen for the data (load audio to memory)
    audio_data = r.record(source)
    
    # Recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    
    # Print the recognized text
    print(text)
