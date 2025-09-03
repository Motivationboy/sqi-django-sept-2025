from django.urls import path

from .import views



urlpatterns = [
    path('',views.homepage,name="homepage"),
    path('services/',views.services_page,name="services_page"),
    path('help/',views.help_page,name="help_page"),
]