
from django.urls import path, include
from django.conf import settings
import os
import sys
from django.contrib import admin
import sys
sys.path.append(r'C:\Users\Huawei MateBook D14\Desktop\S4\Big data\Patented-search-site-with-n-gram-search-engine-using-Kipris-data\Whoosh_django\django1\search')
import views

# Obtenez le chemin absolu du répertoire contenant asgi.py
asgi_path = os.path.dirname(__file__)

# Ajoutez le chemin absolu du répertoire parent au chemin de recherche Python
sys.path.append(os.path.join(asgi_path, '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django1.settings')

urlpatterns = [
    path('', include('search.urls')),
    path('admin/', admin.site.urls),
]

