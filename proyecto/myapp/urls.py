from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.hello),
    path('informacion/', views.info),
]