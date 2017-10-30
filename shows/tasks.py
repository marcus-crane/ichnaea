from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from celery import shared_task

from .models import Show, Season, Episode

import requests

@shared_task
def fetch_show(tmdb_id):
    """ Imports show details from TheMovieDB """
    try:
        headers = { 'User-Agent': 'Ichnaea v0.1 <marcus@thingsima.de>' }
        url = 'https://api.themoviedb.org/3/tv/{}?api_key={}'.format(tmdb_id, settings.TMDB_KEY)
        r = requests.get(url, headers=headers)
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
    except Exception as error:
        return error

@shared_task
def fetch_season(tmdb_id, season_number):
    """ Import season details from TheMovieDB """
    show = Show.objects.get(tmdb_id=tmdb_id)
    try:
        headers = { 'User-Agent': 'Ichnaea v0.1 <marcus@thingsima.de>' }
        url = 'https://api.themoviedb.org/3/tv/{}/season/{}?api_key={}'.format(tmdb_id, season_number, settings.TMDB_KEY)
        r = requests.get(url, headers=headers)
        season_data = r.json()

        name = season_data['name']
        season_number = season_data['season_number']
        airdate = season_data['air_date']
        overview = season_data['overview']

        season = Season.objects.create(show=show, name=name,
                season_number=season_number, airdate=airdate, overview=overview)

        for episode in season_data['episodes']:
            name = episode['name']
            episode_number = episode['episode_number']
            airdate = episode['air_date']
            overview = episode['overview']

            Episode.objects.create(season=season, airdate=airdate, name=name,
                    overview=overview, episode_number=episode_number)

        return "Successfully imported Season {} of {} from TMDB".format(season_number, show.name)
    except Exception as error:
        return error