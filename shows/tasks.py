from django.conf import settings
from celery import shared_task

from .models import Show

import requests

logger = get_task_logger(__name__)

@shared_task
def import_show(tmdb_id):
    """ Imports show details from TheMovieDB """
    r = requests.get('https://api.themoviedb.org/3/tv/{}?api_key={}'.format(tmdb_id, settings.TMDB_KEY))
    show = r.json()

    name = show['name']
    episodes = show['number_of_episodes']
    seasons = show['number_of_seasons']
    languages = show['languages']
    overview = show['overview']

    Show.objects.create(tmdb_id=tmdb_id, name=name, episodes=episodes, seasons=seasons, language=language, overview=overview)

    return "Successfully imported {} from TMDB".format(show.name)
