from flask import Flask, request, render_template, session
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'ThisIsNotARealSecretKey'

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method == 'POST':
        guess =int(request.form['guess'])
        magic_number = int(session['magic_number'])
        still_guessing = True
        if guess < magic_number:
            session['low_value'] = guess
            message = f"(guess) is too low!"
        elif guess > magic_number:
            session['high_value'] = guess
            message = f"(guess) is too high!"
        elif guess == magic_number:
            message = f"Congratulation (guess) is correct!"
        else:    
            message = "Please enter a valid input"
        
    else:
        session["low_value"] = 1
        session["high_value"]= 50
        session["magic_number"] = random.randint(session['low_value'], session['high_value'])
        still_guessing = True

        message = ''

    return render_template('index.html', message = message, still_guessing = still_guessing)

if __name__ == '__main__':
    app.run()
