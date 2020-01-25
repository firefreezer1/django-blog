from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.blog_form, name='blog_form'),
    path('post/<slug:post_uuid>/', views.post_page, name='post_page'),
]
