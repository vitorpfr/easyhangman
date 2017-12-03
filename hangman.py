from flask import Flask, render_template, request, url_for, redirect
import random
app = Flask(__name__)

global gameinprogress
gameinprogress = False

@app.route('/')
def index():
    global words
    global word
    global answer
    global length
    global gameinprogress
    words = ['banana','apple','napkin','subway','outback','pepperoni','cheese','card','spaghetti','bohemian','weather','christmas','garlic']
    word = list(random.choice(words))
    answer = list(len(word)*"_")
    length = str(len(answer))
    gameinprogress = True
    return render_template('index.html', word = "".join(word), answer = "".join(answer), length = length)

@app.route('/game',methods = ['POST', 'GET'])
def game2():
   global gameinprogress
   if gameinprogress == False or request.method != 'POST':
       return redirect(url_for('index'))
   else:
       if request.method == 'POST':
           letter = request.form['letter'].lower()
           for i, item in enumerate(word):
               if item == letter:
                   answer[i] = item
           if word != answer:
               return render_template('game.html', word = "".join(word), answer = "".join(answer), letter = letter)
           else:
               gameinprogress = False
               return render_template('result.html', word = "".join(word))

if __name__ == '__main__':
   app.run('0.0.0.0', 80, debug = True)
