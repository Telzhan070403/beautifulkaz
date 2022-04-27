from django.urls import path
from . import views   # точка vıews тын ишинен гана алады
from .views import *


urlpatterns = [
    path('home/', views.index),
    path('', views.home),
    path('about/', views.about),
    path('menu/', views.menu),
    path('actors/', views.actors),
    path('singers/',views.singers),
    path('films/',views.films),
    path('aboutus/',views.aboutus),
    path('insert/', views.insert),
    path('login/' ,views.addpage , name='login'),
    path('register/' ,views.addpage , name='register'),
    path('post/<int:post_id>',views.show_id, name='post'),
    path('post/<slug:post_slug>',views.show_post,name='post'),
    path('singers/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    path('singers/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    path('singers/<int:pk>/delete', views.NewsDeleteView.as_view(), name='news-delete'), 
    path('send/',send_message),
    
    
]
