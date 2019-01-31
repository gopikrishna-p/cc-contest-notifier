from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/test')
def hello_admin():
   return 'Hello'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)
