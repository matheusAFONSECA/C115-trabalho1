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
                "1": "Verificar saldo",
                "2": "Verificar minutos",
                "3": "Verificar SMS",
            },
        }
    elif number == 2:
        response = {
            "message": "Phase 2",
            "options": {
                "1": "Verificar saldo",
                "2": "Verificar minutos",
                "3": "Verificar SMS",
            },
        }
    elif number == 3:
        response = {
            "message": "Serviço indisponível, por favor, tente novamente mais tarde.",
            "options": "Nehuma opção disponível",
        }
    else:
        response = {
            "message": "Escolha invalida",
        }

    return jsonify(response)


if __name__ == "__main__":
    app.run()
