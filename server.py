from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def dojos ():
    return render_template("index.html")

@app.route('/process.php', methods=['POST'])


def create_user():
   
   print request.form
   name = request.form['name']
   return redirect('/') 

app.run(debug=True) 

