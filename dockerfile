FROM python:3.9-slim

WORKDIR /app
COPY . /app

# Mettre à jour pip
RUN pip install --upgrade pip

# Installer les dépendances système nécessaires (par exemple, pour psycopg2)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 8001

# Commande pour exécuter le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
