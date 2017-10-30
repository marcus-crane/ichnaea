from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Show, Season, Episode

class IndexView(generic.ListView):
  template_name = 'shows/index.html'
  context_object_name = 'shows'

  def get_queryset(self):
    return Show.objects.all()

def seasons(request, slug):
  show = get_object_or_404(Show, slug=slug)
  seasons = Season.objects.filter(show=show)
  episodes = Episode.objects.filter(season=seasons[0])
  context = {'seasons': seasons, 'episodes': episodes}
  return render(request, 'shows/seasons.html', context)