from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect
import calendar
from calendar import HTMLCalendar

from .models import Event, Venue, Tag
from .forms import VenueForm


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.title()
    month_number = list(calendar.month_name).index(month)

    clndr = HTMLCalendar().formatmonth(year, month_number)

    return render(request, 'events/home.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'clndr': clndr
    })


def all_events(request):
    event_list = Event.objects.all()

    month = datetime.now().strftime('%B').title()
    month_number = list(calendar.month_name).index(month)

    clndr = HTMLCalendar().formatmonth(datetime.now().year, month_number)

    return render(request, 'events/all_events.html', {
        'event_list': event_list,
        'clndr': clndr
    })


def all_venues(request):
    venue_list = Venue.objects.all()

    return render(request, 'events/all_venues.html', {
        'venue_list': venue_list
    })


def add_venue(request):
    form = VenueForm()
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        if 'submitted' in request.GET:
            submitted = True
        return render(request, 'events/add_venue.html', {
            'form': form,
            'submitted': submitted
        })


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    tags = Tag.objects.all()
    return render(request, 'events/show_venue.html', {
        'venue': venue,
        'tags': tags
    })
