from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask is installed and working!"


@app.route("/telefonia", methods=["POST"])
def phase():
    data = request.get_json()
    number = data["escolha"]

    if number == "1":
        response = {
            "message": "Você irá ver sobre a situação do seu telefone",
            "options": {
                "1": "Verificar plano atual",
                "2": "Verificar minutos/SMS disponíveis",
                "3": "Verificar faturas",
                # "4": "TESTE",
            },
        }
    elif number == "1Verificar plano atual":
        response = {
            "message": "O seu Plano atual é o Vivo Controle 4GB",
            "options": "None",
        }
    elif number == "1Verificar minutos/SMS disponíveis":
        response = {
            "message": "Ainda restam 100 minutos e 50 SMS",
            "options": "None",
        }
    elif number == "1Verificar faturas":
        response = {
            "message": "A sua fatura atual é de R$ 62,50",
            "options": "None",
        }


    elif number == '2':
        response = {
            "message": "Você irá ver sobre a situação da sua internet",
            "options": {
                "1": "Verificar plano atual",
                "2": "Verificar quantidade de GB disponível",
                "3": "Verificar faturas",
            },
        }
    elif number == "2Verificar plano atual":
        response = {
            "message": "O seu plano de internet atual é o Vivo Fibra 500MB",
            "options": "None",
        }
    elif number == "2Verificar quantidade de GB disponível":
        response = {
            "message": "Ainda restam 100GB",
            "options": "None",
        }
    elif number == "2Verificar faturas":
        response = {
            "message": "A sua fatura atual é de R$ 125,30",
            "options": "None",
        }


    elif number == '3':
        response = {
            "message": "Serviço indisponível no momento.",
            "options": "Nehuma opção disponível",
        }
    else:
        response = {
            "message": "Escolha invalida",
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
