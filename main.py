from flask import Flask, request, render_template
import random

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        guess =request.form['guess']
        if guess < magic_number:
            low_value = guess
            message = f"(guess) is too low!"
        elif guess > magic_number:
            high_value = guess
            message = f"(guess) is too high!"
        elif guess == magic_number:
            message = f"Congratulation (guess) is correct!"
        else:    
            message = "Please enter a valid input"
        still_guessing = True
    else:
        low_value = 1
        high_value = 50
        magic_number = random.randint(low_value, high_value)
        still_guessing = True

        message = ''

    return render_template('index.html', message = message,
        low_value = low_value, high_value = high_value, still_guessing = still_guessing)

if __name__ == '__main__':
    app.run()
