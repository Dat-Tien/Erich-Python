
from django.urls import path
from . import views

urlpatterns = [
    path('', views.personalAddress_get, name='personalAddress_get'),
    path('create/', views.personalAddress_create, name='personalAddress_create'),
    path('update/<int:id>/', views.personalAddress_update, name='personalAddress_update'),
    path('detail/<int:id>/', views.personalAddress_detail, name='personalAddress_detail'),
    path('delete/<int:id>/', views.personalAddress_delete, name='personalAddress_delete'),
]