import os

from flask import Flask, render_template, request
from dotenv import load_dotenv

import azure_cv_handler

app = Flask(__name__)
load_dotenv()


@app.route('/', methods=['GET'])
def index():
    description = 'Upload an image to continue'
    return render_template('index.html', description=description)


@app.route('/generate_image', methods=['POST'])
def generate_image():
    # Picks the image from the form
    file = request.files['image']

    # Creates the azure_cv_handler object
    az = azure_cv_handler.az_api_handler(subscription_key=os.getenv('API_KEY'), endpoint=os.getenv('API_ENDPOINT'))
    description = az.recognize_image(file)
    print(description)

    return description


if __name__ == '__main__':
    app.run(debug=True)
