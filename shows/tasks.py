from django.conf import settings
from django.utils.text import slugify

from .models import Show, Episode

import tvdb_api
t = tvdb_api.Tvdb()

def create_show(show):
    tvdb_id = show['id']
    name = show['seriesName']
    slug = slugify(name)
    poster = show['banner']
    debut = show['firstAired']
    overview = show['overview']
    seen = False
    status = show['status']
    network = show['network']

    try:
        return Show.objects.create(
            tvdb_id=tvdb_id, name=name, slug=slug, poster=poster, debut=debut,
            overview=overview, seen=seen, status=status, network=network)
    except:
        print('Sorry, that show already exists')

def create_episode(episode, show):
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
    
    show = t[name]
    show_entry = create_show(show.data)
    for season in show.keys():
        for episode in show[season].keys():
            ep = show[season][episode]
            create_episode(ep, show_entry)