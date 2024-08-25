from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Flask is installed and working!'

@app.route('/telefonia', methods=['POST'])
def phase():
    data = request.get_json()
    number = data['escolha']
    
    if number == 1:
        response = {'message': 'Phase 1'}
    elif number == 2:
        response = {'message': 'Phase 2'}
    elif number == 3:
        response = {'message': 'Serviço indisponível, por favor, tente novamente mais tarde.'}
    else:
        response = {'message': 'Escolha invalida'}
    
    return jsonify(response)

if __name__ == '__main__':
    app.run()