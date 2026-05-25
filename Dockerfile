# On part d'un Linux léger avec Python
FROM python:3.9-slim

# On crée un dossier de travail dans le conteneur
WORKDIR /app

# On copie le fichier des prérequis et on installe Flask
COPY requirements.txt .
RUN pip install -r requirements.txt

# On copie notre code
COPY app.py .

# On lance l'application
CMD ["python", "app.py"]