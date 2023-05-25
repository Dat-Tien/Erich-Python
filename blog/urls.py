
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get, name='get'),
    path('create/', views.blogCreate, name='create'),
    path('update/<int:id>/', views.blogUpdate, name='update'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('delete/<int:id>/', views.delete, name='delete'),
]