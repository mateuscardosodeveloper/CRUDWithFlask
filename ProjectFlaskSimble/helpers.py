import os
from flask import send_from_directory
from jogoteca import app


def recupera_imagem(id):
    for name_image in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in name_image:
            return name_image

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)