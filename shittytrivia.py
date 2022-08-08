import numpy as np
import math
mu = 2500
sigma = 1000

global correct_answers
correct_answers = 0
global incorrect_answers
incorrect_answers = 0


def get_celebrity():
    s = np.random.normal(mu, sigma, 1)
    print(s)
    if s < 0:
        s = 0
    else:
        s = math.floor(s)
    with open('actors.tsv') as infile:
        for i, line in enumerate(infile):
            if i == s:
                name, link, pic = line.strip().split('\t')
                print(i, name)
                return i, name, link, pic

def is_correct(guess, actor):
    guess = guess.lower().strip()
    actor = actor.lower().strip()
    if guess == actor:
        return True
    return False

from flask import render_template, request, Flask

app = Flask(__name__, template_folder="html")


@app.route('/')
def hello():
    global actor
    index, actor, link, pic = get_celebrity()
    return render_template('shitty.html',pic=pic, correct_answers=correct_answers, incorrect_answers=incorrect_answers)

@app.route('/', methods=['POST'])
def my_form_post():
    global correct_answers
    global incorrect_answers
    text = request.form['text']
    guess = text
    if is_correct(guess, actor):
        correct_answers += 1
    else:
        incorrect_answers += 1
    return hello()



if __name__ == "__main__":
    app.run()
