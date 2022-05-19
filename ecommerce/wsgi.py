"""
WSGI config for ecommerce project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
#WSGI-Web Server Gateway Interface 是 Python 定義網頁程式和伺服器溝通的介面,
#讓Heroku的服務能夠透過這個介面與我們的網站溝通
import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

#application = get_wsgi_application()
application = Cling(get_wsgi_application())