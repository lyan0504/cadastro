from flask import Flask, jsonify, request

app = Flask (__name__)

usuarios = [
    {
        'email' : rodrigues@gmail.com,
        'senha' : '5782546',
    },
    
    {
       'email' : rodrigueslima@gmail.com,
        'senha' : '5788752546',
    },

    {
       'email' : rodriguesfarias@gmail.com,
        'senha' : '578256546',
    },
]
@app.route('/email', methods=['GET'])
def consultar_email():
    return jsonify(email)

@app.route('/email/<int:id>', methods=['GET'])
def consultar_emial_por_id(id):
    for email in email:
        if email.get('id') == id:
            return jsonify(email)


@app.route('/usuarios', methods=['POST'])
def cadastrar_usuario () :
    novo_usaurio = request.get_json()
    usuarios.append (novo_usaurio)
    return jsonify (usuarios)

@app.route('/usuarios/<int:id>', methods=['PUT'])
def atualizar_por_id(id):
    usuario_atualizado = request.get_json()
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            usuarios[indice].update(usuario_atualizado)
            return jsonify(usuarios[indice])

@app.route('/usuarios/<int:id>', methods=['DELETE'])
def excluir_usuario_por_id(id):
    for indice,usuario in enumerate(usuarios):
        if usuario.get('id') == id:
            del usuarios[indice]
    return jsonify(usuarios)

app.run(port=8080,host='localhost',debug=True)

