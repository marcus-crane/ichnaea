from django.db import models

class Show(models.Model):
  tmdb_id = models.IntegerField('TheMovieDB ID Number')
  name = models.CharField('Show title', max_length=200)
  slug = models.SlugField('URL shortcut', max_length=40)
  language = models.CharField('Language', max_length=50, blank=True)
  episodes = models.IntegerField('Number of episodes', blank=True)
  seasons = models.IntegerField('Number of seasons', blank=True)
  overview = models.TextField('General overview', blank=True)
  imported = models.DateField('First imported', blank=True, null=True)