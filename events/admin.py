from django.contrib import admin
from .models import Venue
from .models import MyUser
from .models import Event
from .models import Tag

admin.site.register(Tag)


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'date_added')  # Which fields to show
    ordering = ('name',)
    sortable_by = ('date_added', 'name', 'city')
    search_fields = ('name', 'city')
    list_filter = ('city', 'date_added')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'event_date', 'description', 'manager')
    list_display = ('name', 'event_date', 'venue')  # Which fields to show
    list_filter = ('manager', 'event_date', 'venue')
    ordering = ('-event_date',)  # reverse order


@admin.register(MyUser)
class MyUserAdmin(admin.ModelAdmin):
    fields = ('fullname', 'username', 'email')
    list_display = ('fullname', 'username', 'email')  # Which fields to show
    sortable_by = ('fullname', 'username', 'email')
    ordering = ('username',)
    search_fields = ('fullname', 'username', 'email')
