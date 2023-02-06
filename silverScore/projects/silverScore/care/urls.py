from django.urls import path

from . import views

app_name = 'care'

urlpatterns = [
    path('', views.care_list, name='care_list'),  # 요양원 목록 기본
    path('<int:care_id>/', views.care_detail, name='care_detail'),  # 요양원 detail
]