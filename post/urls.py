from django.urls import path
from .views import Homepage, About

urlpatterns = [
    path('about/', About.as_view(), name='about'),
    path('', Homepage.as_view(), name='home')
]