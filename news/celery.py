import os

from celery import Celery 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def api_calls(self):
    