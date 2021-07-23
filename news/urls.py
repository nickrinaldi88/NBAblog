from django.urls import path, include
from . import views
from .views import PostView


urlpatterns = [
    path('', views.index, name='index'),
    # path('blog/', views.main_blog, name='blog'),
    path('test/', views.test, name='test'),
    path('test/submit', views.test, name='test'),
    path('detail/', views.detail, name='detail'),
    path('mainpage/', views.mainpage, name='mainpage'),
    path('main/', views.main, name='main'),
    path('postview/', PostView.as_view()),
    path('', include('frontend.urls'))
]
