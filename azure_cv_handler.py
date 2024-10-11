from azure.cognitiveservices.vision.computervision \
    import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


class AzureAPIHandler:
    """
    A class to handle Azure Computer Vision API requests.

    Attributes:
        computervision_client (ComputerVisionClient): The client for Azure
        Computer Vision API.
    """

    def __init__(self, subscription_key, endpoint):
        """
        Initializes the AzureAPIHandler with the provided subscription key
        and endpoint.

        Args:
            subscription_key (str): The subscription key for Azure Computer
            Vision API.
            endpoint (str): The endpoint for Azure Computer Vision API.
        """
        self.computervision_client = ComputerVisionClient(
            endpoint, CognitiveServicesCredentials(subscription_key))

    def recognize_image(self, image_stream):
        """
        Recognizes and describes an image using Azure Computer Vision API.

        Args:
            image_stream (stream): The image stream to be processed.

        Returns:
            str: The description of the recognized image.
        """
        # Calls API
        description_result = \
            self.computervision_client.describe_image_in_stream(image_stream, language='pt')

        # Obtains captions (descriptions) in API response
        if len(description_result.captions) == 0:
            return "It was not possible to recognize the image"
        else:
            for caption in description_result.captions:
                return caption.text
