from django.urls import path
from aplicativo import views

urlpatterns = [
    path('home/', views.home)
]