from django.db import models
from django.urls import path

from .views import IndexView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView, purgen

urlpatterns = [
    path('', IndexView.as_view(), name="indexcrud"),
    path('add/', CreateProdutoView.as_view(), name='add produto'),
    path('<int:pk>/update/', UpdateProdutoView.as_view(), name='upd produto'),
    path('<int:pk>/delete/', DeleteProdutoView.as_view(), name='del produto'),
    path('<int:pk>/purge/', purgen, name='purge produto'),
]

