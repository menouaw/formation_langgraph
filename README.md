## Introduction

Support d'exercices pour la formation LangGraph.

## Configuration

### Python

Nécessaire:
- Avoir une version de Python >= 3.11
```
python --version
```

### Cloner le dépôt
```
git clone https://github.com/menouaw/formation_langgraph.git
```
// TODO inclure la version zip

### Créer un environnement et installer les dépendances
#### Mac/Linux/WSL
```
$ python -m venv venv
$ source venv/bin/activate (ou `source venv/Script/activate` pour bash sous Windows)
$ pip install -r requirements.txt
```
#### Windows Powershell
```
PS> python -m venv venv
PS> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
PS> venv\scripts\activate
PS> pip install -r requirements.txt
```

### Jupyter Notebook
Nécessaire:
- Avoir [Jupyter Notebook](https://jupyter.org/install) installé)
```
$ jupyter notebook
```

### Clef d'API OpenAI
- Récupérer une clef d'API OpenAI [ici](https://openai.com/index/openai-api/).

### Inscription et configuration de LangSmith
- Inscrivez-vous à LangSmith [ici](https://docs.langchain.com/langsmith/create-account-api-key#create-an-account-and-api-key) et découvrez-en plus sur LangSmith et son utilisation dans votre flux de travail [ici](https://www.langchain.com/langsmith).

### Configuration de LangSmith Studio

- [Studio](https://docs.langchain.com/langsmith/studio) est un IDE pour visualiser et tester les agents depuis le navigateur.
- Pour démarrer le serveur de développement local, exécutez la commande suivante dans le répertoire `/studio` de chaque module :

```
langgraph dev
```

Vous devriez voir la sortie suivante:
```
- 🚀 API: http://127.0.0.1:2024
- 🎨 Studio UI: https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024
- 📚 API Docs: http://127.0.0.1:2024/docs
```

Accéder à l'interface Studio depuis: `https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024`.

/!\ Ne pas oublier de configuer le fichier `.env` pour chaque `module-x/studio`.
