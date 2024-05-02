from flask import Flask, jsonify, request
import uuid


agendaApp = Flask(__name__)

agenda = []

@agendaApp.route("/")
def home():
    return "<h1>Minha agenda<h1>"

@agendaApp.route("/contacts", methods=["GET"])
def get_contacts():
    return jsonify({"agenda": agenda})

    
@agendaApp.route("/contacts/<int:contact_id>", methods=["GET"])
def get_contact(contact_id):
    for contact in agenda:
        if contact["id"] == contact_id:
            return jsonify({"contact": contact}), 200
    return jsonify({"error": "Contato não encontrado"}), 404


@agendaApp.route("/contacts", methods=["POST"])

def adiciona():  # Recebe os dados JSON da requisição  
    data = request.json 
    id_unico = str(uuid.uuid4()) # Gera um ID único usando uuid
    pessoa={
        "id":id_unico,
        "nome":data["nome"],
        "email":data["email"],
        "telefone":data["telefone"],
        "idade":data["idade"]
    } # Cria um novo contato com os dados fornecidos
    agenda.append(pessoa)# Adiciona o novo contato à agenda
    return jsonify({"message": "Contato criado com sucesso!"}), 201 # Retorna uma mensagem de sucesso com o código de status 201 (Created)

@agendaApp.route("/contacts/<string:contact_id>", methods=["PUT"])
def update_contact(contact_id):
    data = request.json
    for contact in agenda:
        if contact["id"] == contact_id:
            # Atualiza os campos do contato com os novos dados
            contact["nome"] = data["nome"]
            contact["email"] = data["email"]
            contact["telefone"] = data["telefone"]
            contact["idade"] = data["idade"]
            return jsonify({"message": "Contato atualizado com sucesso!"}), 200
    return jsonify({"error": "Contato não encontrado"}), 404



# def verifica_pessoa(agenda, pessoa):
#     return pessoa in agenda.keys()

# def add_pessoa(agenda):
#     pessoa = input("digite o nome da pessoa: ")
#     telefone = input("digite o telefone: ")
#     idade = input("digite a idade: ")
#     adiciona (agenda, pessoa, telefone, idade)

# adiciona(agenda, "Thiago", 230657, 29)
# print(consulta(agenda,"Thiago"))

# add_pessoa(agenda)
@agendaApp.route("/contacts/check", methods=["POST"])
def check_contact():
    # Recebe os dados JSON da requisição
    data = request.json
    
    # Percorre todos os contatos na agenda
    for contact in agenda:
        # Verifica se o nome e o email do contato correspondem aos fornecidos na requisição
        if contact["nome"] == data["nome"] and contact["email"] == data["email"]:
            # Retorna uma mensagem indicando que a pessoa já está na base de dados, com o status 200 (OK)
            return jsonify({"message": "Pessoa já está na base de dados!"}), 200
    
    # Se nenhum contato corresponder aos dados fornecidos, retorna uma mensagem indicando que a pessoa não foi encontrada na base de dados, com o status 404 (Not Found)
    return jsonify({"message": "Pessoa não encontrada na base de dados"}), 404


# verifica_nome = input("Verifique os dados de:")
# print(verifica_pessoa(agenda, verifica_nome))


if __name__ == "__main__":
    agendaApp.run(debug=True)