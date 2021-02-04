from flask import Flask, render_template ,request, url_for, redirect, Response
import numpy as np

app = Flask(__name__)

import os


@app.route('/')
def index():
    return render_template('index.html')
    
    
@app.route('/predict',methods=['POST','GET','PUT'])
def work():
    converted_audio = request.form.get("result_id")
    '''
    if os.path.exists("static"):
        if os.path.exists(f"static/{converted_audio}.mp3"):
            os.remove(f"static/{converted_audio}.mp3")
            os.rmdir("static")
        else:
            os.rmdir("static")
    else:
        os.mkdir("static")
    '''
    from gtts import gTTS 
    text = request.form['text']

    myobj = gTTS(text=text, lang='en', slow=False) 
    myobj.save(f"static/{converted_audio}.mp3")
    
    
    return render_template("index.html", audio = converted_audio)
    
    os.remove(f"static/{converted_audio}.mp3")
    
if __name__=='__main__':
    app.run(debug=True)