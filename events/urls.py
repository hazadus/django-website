from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<int:year>/<str:month>/', views.home, name='home'),
    path('events/', views.all_events, name='all_events'),
    path('venues/', views.all_venues, name='all_venues'),
    path('add_venue/', views.add_venue, name='add_venue'),
    path('venue/<venue_id>/', views.show_venue, name='show_venue'),
    path('search/', views.search_venues, name='search_venues')
]
