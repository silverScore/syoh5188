from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.index),
    path('common/', auth_views.LoginView.as_view(template_name='common/main.html'), name='login'),
]
