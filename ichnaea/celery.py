import os
from celery import Celery
from django.conf import settings

# Set the default Django settings module to be used by celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ichnaea.settings')
app = Celery('ichnaea')

# Avoid pickling the object when using Windows
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
