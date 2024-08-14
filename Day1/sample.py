from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to Flask'

@app.route('/showdetails')
def showdetails():
    return 'Logesh G - 7376222CB128'

if __name__ == '__main__':
    app.run(debug=True)
