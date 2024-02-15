from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_form, name='display_form'),
    path('hide_secret/', views.display_form, name='secret_string'),
    path('reveal_secret/', views.reveal_secret, name='reveal_secret'),
]
