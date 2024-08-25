from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def hello():
    return "Flask is installed and working!"


@app.route("/telefonia", methods=["POST"])
def phase():
    data = request.get_json()
    number = data["escolha"]

    if number == 1:
        response = {
            "message": "Você irá ver sobre a situação do seu telefone",
            "options": {
                "1": "Verificar plano atual",
                "2": "Verificar minutos/SMS disponíveis",
                "3": "Verificar faturas",
            },
        }
    elif number == 2:
        response = {
            "message": "Você irá ver sobre a situação da sua internet",
            "options": {
                "1": "Verificar plano atual",
                "2": "Verificar quantidade de GB disponível",
                "3": "Verificar faturas",
            },
        }
    elif number == 3:
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
    app.run()
