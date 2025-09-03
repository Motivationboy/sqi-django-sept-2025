from django.shortcuts import render, HttpResponse

# Create your views here.

def shop_home(request):
    return HttpResponse("Welcome to the Shop Home")



def shop_cart(request):
    return HttpResponse("Your shopping cart is empty")



# shop /shop/ → returns: "Welcome to the Shop Home" /shop/cart/ → returns: "Your shopping cart is empty"