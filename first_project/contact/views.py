from django.shortcuts import render, HttpResponse

# Create your views here.



def ring_us(request):
    return HttpResponse("ring us: +2348164802689")

def email_us(request):
    return HttpResponse("email us: olapython@gmail.com")