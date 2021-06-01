from flask import Flask, render_template, request

#create a flask instanc
app = Flask(__name__)

#create  a route decorator
@app.route('/', methods=["POST", "GET"])

#route to home page in template
def index():
    return render_template("index.html")
