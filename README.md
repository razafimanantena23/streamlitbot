# streamlitbot
Un clone simplifié de ChatGPT construit avec [Streamlit](https://streamlit.io) et l'[API OpenAI](https://platform.openai.com/).


## Groupe :

Razafimanantena Iriantsoa  
Delage Julia  
Hachi Yousra

## Fonctionnalités

- **Sélection du modèle GPT** : Choisissez parmi différents modèles OpenAI (`gpt-3.5-turbo`, `gpt-3.5-turbo-instruct`, etc.).
- **Limitation des tokens** : Ajustez dynamiquement le nombre maximum de tokens pour chaque réponse.
- **Conversation interactive** : Maintient un historique des messages dans une interface utilisateur conviviale.

## Pré-requis

Avant de commencer, assurez-vous que vous avez les éléments suivants installés sur votre machine :

- Python 3.11 ou plus
- Une clé API valide pour OpenAI

## Installation

1. Clonez ce dépôt sur votre machine locale :
```
git clone https://github.com/razafimanantena23/streamlitbot.git
cd streamlitbot
 ```

2. Créez un environnement virtuel Python et activez-le :
 ```
 python -m venv stenv
 source stenv\Scripts\activate
 ```

3. Installez les libraries nécessaires:
```
pip install -r requirements.txt
```

5. Ajoutez votre clé API OpenAI dans un fichier secrets.toml :
- Créez un dossier .streamlit dans le répertoire 
- Ajoutez un fichier secrets.toml dans ce dossier :
```
[secrets]
OPENAI_API_KEY = "votre_clé_API"
```

## Utilisation
Pour lancer l'application Streamlit, exécutez la commande suivante dans votre terminal :
```
streamlit run chatbotgpt.py
```



