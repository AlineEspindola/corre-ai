FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    libmariadb-dev-compat \
    libmariadb-dev \
    curl \
    unzip \
    wget \
    gnupg \
    ca-certificates \
    fonts-liberation \
    libnss3 \
    libxss1 \
    libasound2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libgbm1 \
    xdg-utils \
    chromium \
    chromium-driver \
    && pip install --upgrade pip

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

COPY . /var/www/html/
WORKDIR /var/www/html/

RUN pip install mysql-connector-python beautifulsoup4 requests selenium

CMD ["python3", "scrapers/onsportsoficial_scraper.py"]
