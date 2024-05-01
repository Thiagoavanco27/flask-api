 # coding: utf-8
from flask import Flask, jsonify, request

app = Flask(__name__)

usuarios = [
    {"nome":"Thiago","id":1,"email":"thiago@email"},
    {"nome":"Joao", "id":2, "email":"joao@email"}
]


@app.route("/")


def first():
    return "<h1> Minha aplicação Flask<h1>"


@app.route("/users", methods=["GET"])

def get_users():
    return jsonify({"usuarios": usuarios})


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    for usuario in usuarios:
        if usuario["id"] == user_id:
            return jsonify({"usuario": usuario}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404


@app.route("/users", methods=["POST"])

def create_user():    
    data = request.json
    usuario={
        "id":len(usuarios) + 1,
        "nome":data["nomeUser"],
        "email":data["emailUser"]
    }
    usuarios.append(usuario)
    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    # Recebe os dados JSON da requisição
    data = request.json
    
    # Percorre a lista de usuários
    for usuario in usuarios:
        # Verifica se o ID do usuário corresponde ao ID fornecido na URL
        if usuario["id"] == user_id:
            # Atualiza o nome do usuário com o valor fornecido no JSON ou mantém o mesmo nome se não houver alteração
            usuario["nome"] = data.get("nomeUser", usuario["nome"])
            # Atualiza o email do usuário com o valor fornecido no JSON ou mantém o mesmo email se não houver alteração
            usuario["email"] = data.get("emailUser", usuario["email"])
            # Retorna uma resposta de sucesso
            return jsonify({"message": "Usuário atualizado com sucesso!"}), 200
    
    # Se o usuário com o ID especificado não for encontrado, retorna um erro 404
    return jsonify({"error": "Usuário não encontrado"}), 404

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    #deleta um usuario
    data = request.json
    
    # Percorre a lista de usuários
    for usuario in usuarios:
        # Verifica se o ID do usuário corresponde ao ID fornecido na URL
        if usuario["id"] == user_id:
            # Deleta o nome do usuário com o valor fornecido no JSON ou mantém o mesmo nome se não houver alteração
            usuarios.remove(usuario)
        return jsonify({"message": "Usuário removido com sucesso!"}), 200
    
    # Se o usuário com o ID especificado não for encontrado, retorna um erro 404
    return jsonify({"error": "Usuário não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)