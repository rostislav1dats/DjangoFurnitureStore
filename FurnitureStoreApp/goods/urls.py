from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.view_catalog, name='catalog'),
    path('product/', views.view_product, name='product'),
]