from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import PostModel

# Create your views here.

class Homepage(ListView):
    model = PostModel
    template_name = 'post/home.html'
    context_object_name = 'post'


class About(TemplateView):
    template_name = 'post/about.html'