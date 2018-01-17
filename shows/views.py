from django.views import generic

from .models import Show, Episode
from .tasks import sort_show_into_seasons

class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'shows'

    def get_queryset(self):
        return Show.objects.all().order_by('name')

class EpisodeView(generic.ListView):
    template_name = 'shows/episodes.html'
    context_object_name = 'seasons'

    def get_queryset(self):
        return sort_show_into_seasons(self.kwargs['slug'])