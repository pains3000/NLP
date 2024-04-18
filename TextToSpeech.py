# pip install nltk
# pip install gtts
# pip install playsound

from gtts import gTTS
from playsound import playsound

# Text to be converted to speech
mytext = "Welcome to Natural Language programming"
language = "en"

# Create a gTTS object
myobj = gTTS(text=mytext, lang=language, slow=False)

# Save the audio as a file
myobj.save("myfile.mp3")

# Play the audio file
playsound("myfile.mp3")
