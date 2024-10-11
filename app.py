import os
from flask import Flask, render_template, request
import azure_cv_handler


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    Renderiza o template index.html com uma descrição inicial.

    Retorna:
        str: Template HTML renderizado com a descrição inicial.
    """
    descricao = 'Processando...'
    return render_template('index.html', descricao=descricao)


@app.route('/generate_image', methods=['POST'])
def generate_image():
    """
    Lida com a requisição POST para gerar a descrição da imagem.

    Retorna:
        str: Descrição da imagem obtida da API Azure Computer Vision.
    """
    # Pega a imagem do formulário
    arquivo = request.files['image']

    # Cria o objeto AzureAPIHandler
    az = azure_cv_handler.AzureAPIHandler(
        subscription_key=os.getenv('API_KEY'),
        endpoint=os.getenv('API_ENDPOINT')
    )
    descricao = az.recognize_image(arquivo)

    return descricao


if __name__ == '__main__':
    app.run()
    # Descomente para executar em modo de depuração e permitir conexão de qualquer dispositivo
    # ATENÇÃO, USE APENAS EM AMBIENTES DE TESTE
    # app.run(debug=True, host='0.0.0.0', port=5000)
