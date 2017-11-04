# Ichnaea

## What's the name?

I needed a name and a quick google shows that Ichnaea was the Greek Goddess of tracking *wink wink*. It seems that Mozilla have a project with the same name which I only just realised now but oh well, sue me, haha.

As much as I like [trakt](https://trakt.tv), I felt that it's a bit overkill when all I want is a simple TV show tracker.

Most of them also use [tvdb](https://www.thetvdb.com) which doesn't support sports, and by association, wrestling which is a pain in the butt.

Anyway, this is also just an excuse to build a slightly larger project that I can actually get some use out of personally.

## What works?

Fetching data from the [themoviedb](https://themoviedb.org) works for both shows and their seasons.

You can either call the functions directly like so:

```python
from shows.tasks import fetch_show, fetch_season

fetch_show(1234)
fetch_season(1234, 1)
```

The above example will fetch the show information and then fetch the first seasons which is appended to the shows via a many to one relationship

I'll probably write some more about it later.

## Requirements

You'll need Python 3 and to install the used modules like so: `pip install -r requirements.txt`

Once that's done, run the migrations which will create a sqlite3 database:

```python
python manage.py migrate
```

The recommended setup is using a virtual enviornoment

You'll have to manually add shows via `python manage.py shell` and then you can view them under the `/shows` url by running the dev server: `python manage.py runserver`.

It's still very early in development
