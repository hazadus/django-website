from django.urls import path
from . import views

urlpatterns = [
    path('django/', views.home, name='home'),
    path('django/<int:year>/<str:month>/', views.home, name='home'),
]
