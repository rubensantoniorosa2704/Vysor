from azure.cognitiveservices.vision.computervision \
    import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials


class AzureAPIHandler:
    """
    Uma classe para lidar com requisições à API Azure Computer Vision.

    Atributos:
        computervision_client (ComputerVisionClient): O cliente para a API Azure
        Computer Vision.
    """

    def __init__(self, subscription_key, endpoint):
        """
        Inicializa o AzureAPIHandler com a chave de assinatura e o endpoint fornecidos.

        Args:
            subscription_key (str): A chave de assinatura para a API Azure Computer
            Vision.
            endpoint (str): O endpoint para a API Azure Computer Vision.
        """
        self.computervision_client = ComputerVisionClient(
            endpoint, CognitiveServicesCredentials(subscription_key))

    def recognize_image(self, image_stream):
        """
        Reconhece e descreve uma imagem usando a API Azure Computer Vision.

        Args:
            image_stream (stream): O fluxo da imagem a ser processada.

        Returns:
            str: A descrição da imagem reconhecida.
        """
        # Chama a API
        description_result = \
            self.computervision_client.describe_image_in_stream(image_stream, language='pt')

        # Obtém as legendas (descrições) na resposta da API
        if len(description_result.captions) == 0:
            return "Não foi possível reconhecer a imagem"
        else:
            for caption in description_result.captions:
                return caption.text
