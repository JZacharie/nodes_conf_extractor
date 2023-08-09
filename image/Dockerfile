# Utilise l'image de base Python
FROM python:3.8

# Copie le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/requirements.txt

# Définit le répertoire de travail
WORKDIR /app

# Installe les dépendances Python
RUN pip install -r requirements.txt

# Installe kubectl
RUN apt-get update && apt-get install -y apt-transport-https gnupg2
RUN curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add -
RUN echo "deb https://apt.kubernetes.io/ kubernetes-xenial main" > /etc/apt/sources.list.d/kubernetes.list
RUN apt-get update && apt-get install -y kubectl

# Copie le reste du code dans le conteneur
COPY . /app

# Commande par défaut pour exécuter quand le conteneur démarre
CMD [ "python", "app.py" ]
