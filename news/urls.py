from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('blog/', views.main_blog, name='blog'),
    path('test/', views.test, name='test'),
    path('test/submit', views.test, name='test'),
    path('detail/', views.detail, name='detail'),
    path('main/', views.main, name='main'),
    path('index/', views.index, name='index'),
    path('', include('frontend.urls'))
]
