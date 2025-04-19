# Usar uma imagem base com Python
FROM python:3.9-slim

# Atualizar e instalar pacotes necessários
RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    libmariadb-dev \
    && pip install --upgrade pip

COPY . /var/www/html/

WORKDIR /var/www/html/

RUN pip install mysql-connector-python

CMD ["python3", "db_connect.py"]
