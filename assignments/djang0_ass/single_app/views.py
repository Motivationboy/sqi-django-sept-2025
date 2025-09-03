from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"single_app/homepage.html")


def profile_page(request):
    return render(request,"single_app/profile-page.html")

def services_page(request):
    return render(request,"single_app/services-page.html")

def help_page(request):
    return render(request,"single_app/help-page.html")







