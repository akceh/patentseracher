"""
WSGI config for django1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

# Obtenez le chemin absolu du répertoire contenant asgi.py
asgi_path = os.path.dirname(__file__)

# Ajoutez le chemin absolu du répertoire parent au chemin de recherche Python
sys.path.append(os.path.join(asgi_path, '..'))

# Définissez l'environnement Django sur le module de configuration des paramètres
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')

application = get_wsgi_application()
