from django.db import models

class Show(models.Model):
  tmdb_id = models.IntegerField('TheMovieDB ID Number')
  name = models.CharField('Show title', max_length=200)
  slug = models.SlugField('URL shortcut', max_length=40)
  bg_art = models.URLField('Background art URL', blank=True)
  language = models.CharField('Language', max_length=50, blank=True)
  episodes = models.IntegerField('Number of episodes', blank=True)
  seasons = models.IntegerField('Number of seasons', blank=True)
  overview = models.TextField('General overview', blank=True)
  seen = models.BooleanField('Seen this show?', default=False)
  imported = models.DateField('First imported', blank=True, null=True)

  def __str__(self):
    return self.name

class Season(models.Model):
  show = models.ForeignKey(Show, on_delete=models.CASCADE)
  name = models.CharField('Season title', max_length=40)
  season_number = models.IntegerField('Season number')
  season_poster = models.URLField('Season poster URL', blank=True)
  airdate = models.DateField('Season kickoff', blank=True)
  overview = models.TextField('Season overview', blank=True)
  seen = models.BooleanField('Seen this season?', default=False)

  def __str__(self):
    return self.name

class Episode(models.Model):
  season = models.ForeignKey(Season, on_delete=models.CASCADE)
  airdate = models.DateField('Episode airdate', blank=True)
  name = models.CharField('Episode name', max_length=200)
  screenshot = models.URLField('Episode screenshot URL', blank=True)
  overview = models.TextField('Episode overview', blank=True)
  episode_number = models.IntegerField('Episode number')
  seen = models.BooleanField('Seen this episode?', default=False)

  def __str__(self):
    return self.name