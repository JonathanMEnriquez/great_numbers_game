from flask import Flask, render_template, redirect, request, session
import random
app = Flask(__name__)
app.secret_key = "TopSecretPassword"

@app.route('/', methods=['POST', 'GET'])
def game():
    if request.method == 'GET':
        session['winner'] = random.randint(0,101)
        print session['winner']
        return render_template ('index.html')
    elif request.method == 'POST':
        guess = int(request.form['guess'])
        winner = session['winner']
        print winner
        if guess == winner:
            answer = 'YOU WIN!!!'
        elif guess > winner:
            answer = 'TOO HIGH'
        elif guess < winner:
            answer = 'TOO LOW'
        return render_template('index.html', guess = guess, answer=answer, winning = winner)


app.run(debug=True)