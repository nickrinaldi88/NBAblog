from django.urls import path

from . import views
from news.views import blog_post_view

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.main_blog, name='blog'),
    path('test/<int:my_id>/', views.test, name='test'),
    path('detail/', views.detail, name='detail'),
    path('archive/', views.archive, name='archive'),
    path('joke/', views.joke, name='joke'),
    path('blogpost/', blog_post_view),
]
