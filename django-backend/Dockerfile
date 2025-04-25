FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer les dépendances
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Mettre à jour pip
RUN pip install --upgrade pip

# Copier les requirements
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install -r requirements.txt

# Copier le code source
COPY . .

# Exposer le port
EXPOSE 8000

# Lancer le serveur de développement
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]