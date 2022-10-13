from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpResponse  # For different kinds of response
import calendar
from calendar import HTMLCalendar

from .models import Event, Venue, Tag
from .forms import VenueForm, EventForm


def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    month = month.title()
    month_number = list(calendar.month_name).index(month)

    calender = HTMLCalendar().formatmonth(year, month_number)

    event_list = Event.objects.all()
    venue_list = Venue.objects.all()

    return render(request, 'events/home.html', {
        'year': year,
        'month': month,
        'month_number': month_number,
        'event_list': event_list,
        'venue_list': venue_list,
        'clndr': calender
    })


def all_events(request):
    event_list = Event.objects.all().order_by('-event_date')  # Sort by field in reverse order

    month = datetime.now().strftime('%B').title()
    month_number = list(calendar.month_name).index(month)

    calender = HTMLCalendar().formatmonth(datetime.now().year, month_number)

    return render(request, 'events/all_events.html', {
        'event_list': event_list,
        'clndr': calender
    })


def all_venues(request):
    venue_list = Venue.objects.all()

    return render(request, 'events/all_venues.html', {
        'venue_list': venue_list
    })


def all_venues_text(request):  # Generate text file
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=venues.txt'

    venues_list = list()
    venues = Venue.objects.all()
    for venue in venues:
        venues_list.append('{venue}\n{address}\n\n'.format(
            venue=venue.name,
            address=venue.address
        ))

    response.writelines(venues_list)
    return response


def add_venue(request):
    submitted = False
    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue/?submitted=True')
    else:
        form = VenueForm()
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


def edit_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('show_venue', venue.id)
    return render(request, 'events/edit_venue.html', {
        'venue': venue,
        'form': form
    })


def search_venues(request):
    if request.method == 'POST':
        search_text = request.POST['search_text']
        search_results = Venue.objects.filter(name__contains=search_text)
        return render(request, 'events/search_venues.html', {
            'search_text': search_text,
            'search_results': search_results
        })
    else:
        return render(request, 'events/search_venues.html', {})


def add_event(request):
    submitted = False
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event/?submitted=True')
    else:
        form = EventForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'events/add_event.html', {
        'form': form,
        'submitted': submitted
    })


def edit_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('all_events')
    return render(request, 'events/edit_event.html', {
        'event': event,
        'form': form
    })


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('all_events')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('all_venues')
