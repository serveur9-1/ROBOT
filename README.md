# ROBOT

Installation RASA

1. Mise en place de l'environnement Python
Verifier les versions de python et pip installés:

python3 --version
pip3 --version
Si ces packages sont déjà installés, ces commandes doivent afficher les numéros de version pour chaque étape et vous pouvez passer à l'étape suivante.

Sinon, suivez les instructions ci-dessous pour les installer.


macOS
Installez le gestionnaire de paquets Homebrew si vous ne l'avez pas déjà fait.

Une fois que vous avez terminé, vous pouvez installer Python3.

brew update
brew install python

2. Configuration de l'environnement virtuel #
Cette étape est facultative, mais nous vous recommandons vivement d'isoler les projets python à l'aide d'environnements virtuels. Des outils tels que virtualenv et virtualenvwrapper fournissent des environnements Python isolés, qui sont plus propres que l'installation de packages à l'échelle du système (car ils évitent les conflits de dépendances). Ils vous permettent également d'installer des packages sans privilèges root.


macOS
Créez un nouvel environnement virtuel en choisissant un interpréteur Python et en créant un répertoire ./venv pour le contenir:
python3 -m venv ./venv

Activez l'environnement virtuel:

source ./venv/bin/activate

3. Installation de Rasa Open Source#

Assurez-vous d'abord que votre version de pip est à jour:
pip3 install -U pip

installer Rasa Open Source:

pip3 install rasa
