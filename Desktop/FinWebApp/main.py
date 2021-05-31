from flask import Flask, render_template

#create a flask instanc
app = Flask(__name__)

#create  a route decorator
@app.route('/')

#@app.route('/home')
#route to home page in template
def index():
    return render_template("index.html")
