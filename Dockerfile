# Use a imagem oficial do Python 3.12
FROM python:3.12

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copia os arquivos de requisitos para o contêiner
COPY requirements.txt .

# Instala as dependências
RUN pip install -r requirements.txt

# Copia o restante do código para o contêiner
COPY . .

# Define a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

# Expõe a porta onde o serviço Flask será executado
EXPOSE 5000

# Inicia o aplicativo Flask
CMD ["flask", "run"]
