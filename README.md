# Vysor
Vysor é um aplicativo baseado na web que permite aos usuários fazer upload de imagens e receber descrições detalhadas delas. Este projeto é particularmente útil para pessoas com deficiência visual, profissionais de marketing digital e qualquer pessoa que precise de descrições de imagens rápidas e confiáveis.

## Tecnologias utilizadas
- [Microsoft Azure Computer Vision API](https://learn.microsoft.com/pt-br/azure/ai-services/computer-vision/)
- [Flask](https://flask.palletsprojects.com/pt_BR/3.0.x/)
- [Bulma](https://bulma.io/)
- [Docker](https://www.docker.com/)

## Como usar
- Primeiro, você precisa criar uma conta na Azure e configurar um recurso do Azure Computer Vision (não se preocupe, é fácil de configurar e gratuito até 20 chamadas por minuto, 5 mil chamadas por mês). Você pode ler a documentação da API [aqui](https://learn.microsoft.com/pt-br/azure/ai-services/computer-vision/);
- Certifique-se de ter o [Docker](https://www.docker.com/) instalado;
- Insira sua chave de API e endpoint no arquivo ``.env``;
- Execute ```make run``` para construir o container e executá-lo na porta 5000:5000;

- Divirta-se :)

## Como contribuir
- Clone o repositório na sua máquina e crie uma nova branch para sua nova funcionalidade/melhoria.
- Envie um pull request com uma descrição do que você modificou.
