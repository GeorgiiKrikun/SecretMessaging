from django.urls import path, re_path
from . import views

urlpatterns = [
    path('hide_secret/', views.create_secret, name='secret_string'),
    path('reveal_secret/', views.reveal_secret, name='reveal_secret'),
    re_path(r'^.*$', views.redirect_view, name='redirect_view'),

]
