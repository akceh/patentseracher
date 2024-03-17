import os
import sys
from django.core.asgi import get_asgi_application

# Obtenez le chemin absolu du répertoire contenant asgi.py
asgi_path = os.path.dirname(__file__)

# Ajoutez le chemin absolu du répertoire parent au chemin de recherche Python
sys.path.append(os.path.join(asgi_path, '..'))

# Définissez l'environnement Django sur le module de configuration des paramètres
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')

# Obtenez l'application ASGI de Django
application = get_asgi_application()
