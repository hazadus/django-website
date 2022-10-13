from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events/', views.all_events, name='all_events'),
    path('add_event/', views.add_event, name='add_event'),
    path('edit_event/<event_id>/', views.edit_event, name='edit_event'),
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
    path('venues/', views.all_venues, name='all_venues'),
    path('venues/text/', views.all_venues_text, name='all_venues_text'),
    path('venues/csv/', views.all_venues_csv, name='all_venues_csv'),
    path('venue/<venue_id>/', views.show_venue, name='show_venue'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('edit_venue/<venue_id>/', views.edit_venue, name='edit_venue'),
    path('delete_venue/<venue_id>', views.delete_venue, name='delete_venue'),
    path('search/', views.search_venues, name='search_venues'),
]
