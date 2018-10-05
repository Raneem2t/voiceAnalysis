from flask import Flask, flash, redirect, render_template, request
from pyfladesk import init_gui
from routes import *

import speechToText
import Criminal_Words
import AbnormalWord

app = Flask(__name__)

c = Criminal_Words
a = AbnormalWord.cc

@app.route("/user")
def hello():
        s = speechToText
        t = s.convert_speech_to_text()
        # cri = c.find_criminal_words()
        # ab = a

        # return render_template('index.html', **locals())
        return render_template('hello.html', text=t)




if __name__ == "__main__":
    # d.hello()
    app.jinja_env.cache = {}
    init_gui(app)