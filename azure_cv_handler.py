# Importando os módulos necessários
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import pyttsx3
import os

class Vysor:
    def __init__(self):
        # Configura a API de reconhecimento de imagem
        self.subscription_key = "f25980f591a742e5b4d46639a0681234"
        self.endpoint = "https://vysor-vresource.cognitiveservices.azure.com/"
        self.computervision_client = ComputerVisionClient(self.endpoint, CognitiveServicesCredentials(self.subscription_key))
        self.images_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

        # Configura o motor de TTS
        self.engine = pyttsx3.init()

    def reconhecer_imagem(self, imagem):
        # Chamar API
        description_result = self.computervision_client.describe_image_in_stream(imagem, language='pt')

        # Obter as legendas (descrições) da resposta, com nível de confiança
        if len(description_result.captions) == 0:
            self.engine.say("Nenhuma descrição detectada.")
            self.engine.runAndWait()
        else:
            for caption in description_result.captions:
                return caption.text
