from django.views import generic

from .models import Show, Episode

class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'shows'

    def get_queryset(self):
        return Show.objects.all().order_by('name')

class EpisodeView(generic.ListView):
    template_name = 'shows/episodes.html'
    context_object_name = 'episodes'

    def get_queryset(self):
        season = {}
        return Episode.objects.filter(show__name='Better Call Saul')