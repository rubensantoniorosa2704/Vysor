# Importando os módulos necessários
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import pyttsx3
import os

class az_api_handler():
    def __init__(self, subscription_key, endpoint) -> None:
        # Configures Azure Computer Vision API
        self.computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

        # Configures TTS motor
        self.engine = pyttsx3.init()

    def recognize_image(self, imagem) -> str:
        # Calls API
        description_result = self.computervision_client.describe_image_in_stream(imagem, language='pt')

        # Obtains captions (descriptions) in API response
        if len(description_result.captions) == 0:
            return "It was not possible to recognize the image"
        else:
            for caption in description_result.captions:
                return caption.text

    def say_text_out_loud(self, text) -> None:
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()
