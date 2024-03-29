import os

from flask import Flask, render_template, request, session
from dotenv import load_dotenv

import azure_cv_handler

app = Flask(__name__)
load_dotenv()


@app.route('/')
def index():
    teste = 'teste'
    return render_template('index.html')


@app.route('/upload-image', methods=['POST'])
def upload_image():
    image = request.files['image']

    # Creates the azure_cv_handler object
    az = azure_cv_handler.az_api_handler(subscription_key=os.getenv('API_KEY'), endpoint=os.getenv('API_ENDPOINT'))
    response = az.recognize_image(image)
    return render_template('index.html', caption=response)


if __name__ == '__main__':
    app.run()
