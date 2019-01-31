from flask import Flask
app = Flask(__name__)

@app.route("/test")
def hello():
    return render_template('index.html')
