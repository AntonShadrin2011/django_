from django.shortcuts import HttpResponse
from django.shortcuts import render
from . models import Cite
from django.views.generic import ListView, CreateView
from .forms import *

class HomeLV(ListView):
    model = Cite
    template_name = 'd/12345.html'
    paginate_by = 56

class HomeCV(CreateView):
    model = Cite
    template_name = 'd/create.html'
    form_class = CiteFrom

