from django.shortcuts import render,HttpResponse

# Create your views here.


def book_list(request):
    books = ['The Alchemist', '1984', 'To Kill a Mockingbird', 'Moby Dick', 'Pride and Prejudice']
    html = "<ul>" + "".join(f"<li>{book}</li>" for book in books) + "</ul>"
    return HttpResponse(html)

def featured_books(request):
    featured = ['The Little Prince', 'Brave New World']
    html = "<div>" + "".join(f"<p>{book}</p>" for book in featured) + "</div>"
    return HttpResponse(html)
