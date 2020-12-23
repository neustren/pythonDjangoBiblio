from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import Materia


class IndexListView(ListView):
    template_name = 'indexPag.html'
    paginate_by = 4
    model = Materia
    # ordering = 'id'
    ordering = 'nome'
