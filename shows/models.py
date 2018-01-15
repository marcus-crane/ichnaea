from django.db import models

class Show(models.Model):
  SHOW_STATUS = (
    ('Continuing', '📡 Airing'),
    ('Ended', '🏁 Finished'),
  )
  tvdb_id = models.IntegerField()
  name = models.CharField(max_length=100)
  slug = models.SlugField(max_length=100)
  poster = models.URLField(null=True)
  debut = models.DateTimeField()
  overview = models.TextField(null=True)
  seen = models.BooleanField(default=False)
  status = models.CharField(max_length=10, choices=SHOW_STATUS)
  network = models.CharField(max_length=50)

  def __str__(self):
    return self.name

class Episode(models.Model):
  show = models.ForeignKey(Show, on_delete=models.CASCADE)
  tvdb_id = models.IntegerField()
  name = models.CharField(max_length=100)
  number = models.IntegerField()
  season = models.IntegerField()
  aired = models.DateField()
  overview = models.TextField()

  def __str__(self):
    return self.name

