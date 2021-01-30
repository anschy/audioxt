from flask import Flask, render_template ,request, url_for, redirect, Response
import numpy as np

app = Flask(__name__)

import os


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/predict',methods=['POST','GET'])
def work():
    if os.path.exists("temp"):
        if os.path.exists("temp/welcome.mp3"):
            os.remove("temp/welcome.mp3")
            os.rmdir("temp")
        else:
            os.rmdir("temp")
    else:
        pass
    os.mkdir("temp")
    from gtts import gTTS 
    text = request.form['text']
    myobj = gTTS(text=text, lang='en', slow=False) 
    myobj.save("temp/welcome.mp3")
    
    return render_template("index.html", audio = 'temp/welcome.mp3')
    
    def generate():
        with open("temp/welcome.mp3", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-mp3")
    
    
    
if __name__=='__main__':
    app.run(debug=True)