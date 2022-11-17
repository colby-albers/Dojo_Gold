from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)

app.secret_key = "Ozzyisagoodboy"

@app.route('/')
def index():
    if 'your_gold' not in session:
        session['your_gold'] = 0
        print("Your Gold = 0")
        session['process_money'] = []
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():


    if request.form['building'] == 'farm':
        number = random.randint(10,20)
        session['your_gold'] += number
        print(f"Your Gold = {session['your_gold']}")

    elif request.form['building'] == 'cave':
        number = random.randrange(5,10)
        session['your_gold'] += number
        print(f"Your Gold = {session['your_gold']}")

    elif request.form['building'] == 'house':
        number = random.randrange(2,5)
        session['your_gold'] += number
        print(f"Total Gold = {session['your_gold']}")
    
    elif request.form['building'] == 'casino':
            number = random.randrange(-50,50)
            session['your_gold'] += number
            print(f"Your Gold = {session['your_gold']}")

    print(session)
    return redirect('/')

@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True, port=8000)