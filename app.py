import os
from flask import Flask, render_template, request
import azure_cv_handler

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """
    Render the index.html template with an initial description.

    Returns:
        str: Rendered HTML template with the initial description.
    """
    description = 'Processing...'
    return render_template('index.html', description=description)


@app.route('/generate_image', methods=['POST'])
def generate_image():
    """
    Handle POST request to generate image description.

    Returns:
        str: Image description obtained from Azure Computer Vision API.
    """
    # Picks the image from the form
    file = request.files['image']

    # Creates the AzureAPIHandler object
    az = azure_cv_handler.AzureAPIHandler(subscription_key=os.getenv('API_KEY'),
                                          endpoint=os.getenv('API_ENDPOINT'))
    description = az.recognize_image(file)

    return description


if __name__ == '__main__':
    app.run()
    # Uncomment to run in debug mode and to allow connection from any device
    # WARNING, ONLY USE IN TESTING ENVIRONMENTS
    # app.run(debug=True, host='0.0.0.0', port=5000)
