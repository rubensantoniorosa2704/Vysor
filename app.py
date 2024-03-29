import os

from flask import Flask, render_template, request, session
from dotenv import load_dotenv

import azure_cv_handler

app = Flask(__name__)
load_dotenv()


@app.route('/', methods=['GET', 'POST'])
def index():
    description = None
    if request.method == 'POST':
        file = request.files['file']

        # Creates the azure_cv_handler object
        az = azure_cv_handler.az_api_handler(subscription_key=os.getenv('API_KEY'), endpoint=os.getenv('API_ENDPOINT'))
        description = az.recognize_image(file)

    return render_template('index.html', description=description)


if __name__ == '__main__':
    app.run(debug=True)
