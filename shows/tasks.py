from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from celery import shared_task

from .models import Show

import requests

@shared_task
def fetch_show(tmdb_id):
    """ Imports show details from TheMovieDB """
    url = 'https://api.themoviedb.org/3/tv/{}?api_key={}'.format(tmdb_id, settings.TMDB_KEY)
    r = requests.get(url)
    show = r.json()

    name = show['name']
    slug = slugify(name)
    episodes = show['number_of_episodes']
    seasons = show['number_of_seasons']
    language = show['original_language']
    overview = show['overview']
    imported = timezone.now()

    Show.objects.create(tmdb_id=tmdb_id, name=name, slug=slug, episodes=episodes,
            seasons=seasons, language=language, overview=overview, imported=imported)

    return "Successfully imported {} from TMDB".format(name)
