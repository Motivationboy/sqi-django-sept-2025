from django.shortcuts import render, HttpResponse

# Create your views here.

# community/views.py


def events(request):
    events = ['Book Fair - Sept 10', 'Storytelling Night - Sept 15']
    html = "<section>" + "".join(f"<p>{event}</p>" for event in events) + "</section>"
    return HttpResponse(html)
