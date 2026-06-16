from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.product_catalog, name='product_catalog'),
    path('watch/<slug:slug>/', views.product_detail, name='product_detail'),
]