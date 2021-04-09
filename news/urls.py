from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.main_blog, name='blog'),
    path('test/', views.test, name='test'),
    path('detail/', views.detail, name='detail'),
    path('archive/', views.archive, name='archive'),
]
