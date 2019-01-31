from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/test')
def hello_admin():
   return 'Hello'
   
@app.route('/testt')
def hello_user():
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug = True)
