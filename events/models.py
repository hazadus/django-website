from datetime import datetime

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField('Tag Name', max_length=32)

    def __str__(self):
        return f'#{self.name.lower()}'


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=128)
    address = models.CharField('Venue Address', max_length=256)
    city = models.CharField('Location City', max_length=32, blank=True)
    zip_code = models.CharField('Zip Code', max_length=8, blank=True)
    phone = models.CharField('Contact Phone', max_length=16, blank=True)
    description = models.TextField('Description', blank=True)
    how_to_get_there = models.TextField('How to get there (transport, etc.)', blank=True)
    website = models.URLField('Website URL', blank=True)
    banner_pic = models.CharField('Banner Picture Filename', max_length=64, blank=True)
    email = models.EmailField('Contact Email', blank=True)
    date_added = models.DateTimeField('Date Added', blank=False, default=datetime.now())
    tags = models.ManyToManyField(Tag, blank=True)
    yandex_map_widget = models.TextField('Yandex Map Widget', blank=True)
    yandex_reviews_widget = models.TextField('Yandex Reviews Widget', blank=True)

    def __str__(self):
        return self.name


class MyUser(models.Model):
    username = models.CharField('User Login Name', max_length=32)
    fullname = models.CharField('User Full Name', max_length=32)
    email = models.EmailField('User Email')

    def __str__(self):
        return f'{self.fullname}'


class Event(models.Model):
    name = models.CharField('Event Name', max_length=128)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.SET_NULL)
    manager = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    description = models.TextField('Event Description', blank=True)
    attendees = models.ManyToManyField(MyUser, blank=True)

    def __str__(self):
        return self.name
