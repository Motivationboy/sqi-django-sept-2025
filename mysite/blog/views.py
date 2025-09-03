from django.shortcuts import render, HttpResponse


# Create your views here.



def blog_home(request):
    return HttpResponse("Welcome to the Blog Home")


def blog_post(request):
    return HttpResponse("This is blog post #1")


def blog_about(request):
    return HttpResponse("About the Blog" )











# /blog/ → returns: "Welcome to the Blog Home" /blog/post/1/ → returns: "This is blog post #1" /blog/about/ → returns: "About the Blog" App: shop /shop/ → returns: "Welcome to the Shop Home" /shop/cart/ → returns: "Your shopping cart is empty"