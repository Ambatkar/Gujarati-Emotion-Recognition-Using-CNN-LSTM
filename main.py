import Prediction
from flask import Flask, render_template, request, url_for
import os
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html');

@app.route("/predict",methods=['POST'])
def my_post():
    text = request.form['texta']
    px = Prediction.predicted([text])
    print(text," ",px)
    posts ={
        'txt_guj': text,
        'pretext':px
        }
    #processed_text = text.upper()
    return render_template('next.html',export=posts);

if __name__ == '__main__':
    app.run()

'''

x = Prediction.predict(["હું તને પ્રેમ કરું છુ"])

print(x)
'''