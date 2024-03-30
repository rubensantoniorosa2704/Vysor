import os
import pyttsx3

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

class az_api_handler():
    def __init__(self, subscription_key, endpoint) -> None:
        # Configures Azure Computer Vision API
        computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

    def recognize_image(self, image) -> str:
        # Calls API
        description_result = self.computervision_client.describe_image_in_stream(image)

        # Obtains captions (descriptions) in API response
        if len(description_result.captions) == 0:
            return "It was not possible to recognize the image"
        else:
            for caption in description_result.captions:
                return caption.text
