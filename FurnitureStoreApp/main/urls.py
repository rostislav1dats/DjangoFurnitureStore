from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.view_index, name='index'),
    path('about/', views.view_about, name='about'),
]