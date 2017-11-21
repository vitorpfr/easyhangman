from flask import Flask, render_template, request
import random
app = Flask(__name__)

word = list("banana")
answer = list(len(word)*"_")
length = str(len(answer))

@app.route('/')
def index():
    return render_template('index.html', word = "".join(word), answer = "".join(answer), length = length)

@app.route('/game',methods = ['POST', 'GET'])
def game2():
   if request.method == 'POST':
       letter = request.form['letter']
       for i, item in enumerate(word):
           if item == letter:
               answer[i] = item
       if word != answer:
           return render_template('game.html', word = "".join(word), answer = "".join(answer), letter = letter)
       else:
           return render_template('result.html', word = "".join(word))
# final: return render_template('result.html', word = word)

if __name__ == '__main__':
   app.run(debug = True)
