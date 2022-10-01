from django.urls import path, include
from . import views

urlpatterns = [
    path('django/', include([
        path('', views.home, name='home'),
        path('<int:year>/<str:month>/', views.home, name='home'),
        ])),
]
