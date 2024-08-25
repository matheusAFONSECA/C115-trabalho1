from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask is installed and working!'

@app.route('/telefonia', methods=['POST'])
def phase():
    data = request.get_json()
    number = data['escolha']
    
    if number == 1:
        return 'Phase 1'
    elif number == 2:
        return 'Phase 2'
    elif number == 3:
        return 'Phase 3'
    else:
        return 'Escolha invalida'

if __name__ == '__main__':
    app.run()