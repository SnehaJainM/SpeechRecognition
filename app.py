from flask import Flask , render_template, request
 #python pip install flask
from flask import redirect

import speech_recognition as sr #python3 -m pip install SpeechRecognition
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def indexx():
    transcript=""
    if request.method=="POST":
        print("Form data receieved")

        if "file" not in request.files:
            return redirect(request.url) #import redirect
        
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
    
        if file: #add a wav file. 
            recognizer= sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data=recognizer.record(source)
            transcript =  recognizer.recognize_google(data, key=None) #pypi.org/project/SpeechRecognition/
            #wav speech sample  >> Open speech repository. OR convert mp3 to wav format.
    return render_template('index.html',transcript=transcript)


if __name__ == "__main__":
    app.run(debug=True,threaded=True)
