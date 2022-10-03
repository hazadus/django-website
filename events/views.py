from datetime import datetime

from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

from .models import Event, Venue


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
