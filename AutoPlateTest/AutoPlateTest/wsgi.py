"""
WSGI config for AutoPlateTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""
#是Python应用程序或框架和Web服务器之间的一种接口
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AutoPlateTest.settings')

application = get_wsgi_application()
