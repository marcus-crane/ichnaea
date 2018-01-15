from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Show, Episode

class IndexView(generic.ListView):
  template_name = 'shows/index.html'
  context_object_name = 'shows'

  def get_queryset(self):
    return Show.objects.all()