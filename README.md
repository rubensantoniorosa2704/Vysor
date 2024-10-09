# Vysor
Vysor is an web-based application that allows users to upload images and receive detailed descriptions of them. This project is particularly useful for visually impaired individuals, digital marketers, and anyone in need of quick and reliable image descriptions.

## Technologies used
- [Microsoft Azure Computer Vision API](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Bulma](https://bulma.io/)
- [Docker](https://www.docker.com/)

## How to use it
- First of all, you need create an Azure account and configure an Azure Computer Vision Resource (don't worry, it's easy to set up and free up to 20 Calls per minute, 5K Calls per month). You can read the API documentation [here](https://learn.microsoft.com/en-us/azure/ai-services/computer-vision/);
- Make sure to have [docker](https://www.docker.com/) installed;
- Insert you api key and enpoint into the ``.env`` file
- Execute ```make run``` to build the container and run it on 5000:5000 port;

- Have fun :)

## How to contribute
- Clone the repository in your machine, and create a new branch for your new functionality/improvement.
- Send me a pull request with a description of what you modified
