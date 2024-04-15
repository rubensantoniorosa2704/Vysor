# Vysor
Vysor is an web-based application that allows users to upload images and receive detailed descriptions of them. This project is particularly useful for visually impaired individuals, digital marketers, and anyone in need of quick and reliable image descriptions.

## Technologies used
- [Microsoft Azure Computer Vision API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Bulma](https://bulma.io/)

## How to run it
- Clone the repository in your machine
- Fill your Azure Cognitive Vision API key and endpoint in the [.env file](/.env)
- Build the image with ```docker build -t vysor .```.
- Create the container with ```docker run -d -p 5000:5000 --name vysor-container vysor```.
- Open ```localhost:5000``` in your browser to test the site.