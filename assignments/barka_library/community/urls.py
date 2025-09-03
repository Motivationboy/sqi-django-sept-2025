from django.urls import path

from community import views


urlpatterns = [
    path('events/',views.events,name="events"),
]