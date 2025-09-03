from django.urls import path

from catalog import views

urlpatterns = [
    path('',views.book_list,name="book_list"),
    path('special/',views.featured_books,name="feature_books"),
]