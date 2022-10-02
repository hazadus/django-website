from django.db import models


class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=128)
    address = models.CharField('Venue Address', max_length=256)
    zip_code = models.CharField('Zip Code', max_length=8)
    phone = models.CharField('Contact Phone', max_length=16)
    website = models.URLField('Website URL')
    email = models.EmailField('Contact Email')

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField('User Login Name', max_length=32)
    fullname = models.CharField('User Full Name', max_length=32)
    email = models.EmailField('User Email')

    def __str__(self):
        return f'{self.fullname} ({self.username})'


class Event(models.Model):
    name = models.CharField('Event Name', max_length=128)
    event_date = models.DateTimeField('Event Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    manager = models.CharField("Who's In Charge", max_length=64)
    description = models.TextField('Event Description', blank=True)
    attendees = models.ManyToManyField(User, blank=True )

    def __str__(self):
        return self.name
