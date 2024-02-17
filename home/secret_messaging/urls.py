from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_secret, name='index'),
    path('hide_secret/', views.create_secret, name='secret_string'),
    path('reveal_secret/', views.reveal_secret, name='reveal_secret'),
]
