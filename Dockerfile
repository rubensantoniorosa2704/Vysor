FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN python -m venv venv

RUN . venv/bin/activate && pip install -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

EXPOSE 5000

CMD ["/bin/bash", "-c", ". venv/bin/activate && flask run"]
