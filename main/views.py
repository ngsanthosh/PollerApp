from django.shortcuts import render

from django.views.generic import ( ListView,DetailView)
from main import models

class Index(ListView):
    model=models.Question
    template_name="index.html"

class Question(DetailView):
    model=models.Question
    template_name="question.html"
