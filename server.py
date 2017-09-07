from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def ninjaLanding():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    return render_template('ninjas.html')

@app.route('/dojos/new', methods=['GET','POST'])
def dojoNewbies():
    if request.method == 'POST':
        return redirect('/')
    return render_template('dojos/new.html')

app.run(debug=True)
