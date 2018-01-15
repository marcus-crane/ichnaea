from django.conf import settings
from django.utils.text import slugify

from .models import Show, Episode

import tvdbsimple as tvdb
tvdb.KEYS.API_KEY = settings.APIKEY

def create_show(show):
    posters = show.Images.poster()
    
    tvdb_id = show.id
    name = show.seriesName
    slug = slugify(show.seriesName)
    poster = 'https://www.thetvdb.com/banners/_cache/' + posters[0]['fileName']
    debut = show.firstAired
    overview = show.overview
    seen = False
    status = show.status
    network = show.network

    return Show.objects.create(
        tvdb_id=tvdb_id, name=name, slug=slug, poster=poster, debut=debut,
        overview=overview, seen=seen, status=status, network=network)

def create_episodes(episodes, show):
    for episode in episodes:
        number = episode['airedEpisodeNumber']
        season = episode['airedSeason']
        name = episode['episodeName']
        tvdb_id = episode['id']
        aired = episode['firstAired']
        overview = episode['overview']

        Episode.objects.create(
            show=show, number=number, season=season, name=name,
            tvdb_id=tvdb_id, aired=aired, overview=overview)


def fetch_show(name):
    """ 
    Imports show details from TheTVDB

    This function takes a series ID from TVDB and pulls
    various details about the series and submits them to the database

    It just assumes the first result is what you want for now
    """
    
    search = tvdb.Search()
    response = search.series(name)
    show_id = search.series[0]['id']
    show = tvdb.Series(show_id)
    response = show.info()
    
    show_entry = create_show(show)

    episodes = show.Episodes.all()
    create_episodes(episodes, show_entry)