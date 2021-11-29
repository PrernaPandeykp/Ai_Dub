import speech_recognition as sr
import pyttsx3

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('home.html')


@app.route('/')
def hello():
    return 'Hello, World!'

r=sr.Recognizer()
filename="output.wav"
with sr.AudioFile(filename) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)

        

if __name__ == "__main__":
    app.run()
