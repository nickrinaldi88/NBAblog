import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()  # looks for tasks.py in app folder


@app.task(bind=True)
def api_calls(self):
