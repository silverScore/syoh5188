from django.urls import path, include
from django.contrib.auth import views as auth_views  # login&logout
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.index, name='main'),
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),

]