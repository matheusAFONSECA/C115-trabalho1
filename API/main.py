from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask is installed and working!'

if __name__ == '__main__':
    app.run()