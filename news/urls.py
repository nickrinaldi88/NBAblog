from django.urls import path, include
from . import views
from .views import PostView


urlpatterns = [
    path('', views.index, name='index'),
    # path('blog/', views.main_blog, name='blog'),
    path('test/<int:my_id>/', views.test, name='test'),
    path('detail/', views.detail, name='detail'),
    path('archive/', views.archive, name='archive'),
    # path('main/', views.main, name='main'),
    path('postview/', PostView.as_view()),
    path('', include('frontend.urls'))
]
