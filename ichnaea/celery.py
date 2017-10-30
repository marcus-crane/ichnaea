import os
from celery import Celery

# Set the default Django settings module to be used by celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ichnaea.settings')

app = Celery('ichnaea')
app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks()