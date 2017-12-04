from flask import Flask, render_template, request, url_for, redirect
import random
app = Flask(__name__)

# Game hasn't started yet
global gameinprogress
gameinprogress = False

# Game started, variables defined
@app.route('/')
def index():
    global words
    global word
    global answer
    global length
    global gameinprogress
    global selectedletters
    global losecounter
    words = ['banana','apple','napkin','subway','outback','pepperoni','cheese','card','spaghetti','bohemian','weather','christmas','garlic', 'pizza', 'building', 'mountain', 'scheme', 'christ', 'lake', 'business', 'drumstick']
    word = list(random.choice(words))
    answer = list(len(word)*"_")
    length = str(len(answer))
    selectedletters = []
    losecounter = 0
    gameinprogress = True
    return render_template('index.html', word = "".join(word), answer = "".join(answer), length = length)

# Player selected a letter, check if letter exists in the word
@app.route('/game',methods = ['POST', 'GET'])
def game2():
   global gameinprogress
   global selectedletters
   global losecounter
   global pagemessage
   if gameinprogress == False or request.method != 'POST':
       return redirect(url_for('index'))
   else:
       if request.method == 'POST':
           letter = request.form['letter'].lower()
           rightletter = 0
           for i, item in enumerate(word):
               if item == letter:
                   answer[i] = item
                   rightletter = 1
           selectedletters.append(letter)
           if rightletter == 0:
               losecounter += 1
               pagemessage = "The letter " + letter + " is not in this word, select another letter."
           else:
               pagemessage = "Yes! The letter " + letter + " is in the word! Now choose another letter."
           if losecounter == 6:
               return render_template('lost.html', word = "".join(word))
           if word != answer:
               return render_template('game.html', word = "".join(word), answer = "".join(answer), letter = letter, selectedletters = selectedletters, pagemessage = pagemessage)
           else:
               gameinprogress = False
               return render_template('result.html', word = "".join(word))

if __name__ == '__main__':
   app.run('0.0.0.0', 80, debug = True)
