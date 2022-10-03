from django.contrib import admin
from .models import Venue
from .models import MyUser
from .models import Event
from .models import Tag

admin.site.register(MyUser)
admin.site.register(Tag)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'date_added')
    ordering = ('name',)
    sortable_by = ('date_added', 'name', 'city')
    search_fields = ('name', 'city')
    list_filter = ('city', 'date_added')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')
    list_filter = ('manager', 'event_date', 'venue')
    ordering = ('-event_date',)
