from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def index(request):
    return HttpResponse("<h1 style='text-align: center'>Home Page Kolesa</h1>")


def categories(request, categoriesid):
    if request.POST:
        print(request.POST)
    return HttpResponse(f"<h1 style='text-align: center'>Car categories</h1><h1 style='text-align: center'>Sen engizgen san:  {categoriesid}</h1>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1 style='text-align: center'>Нет такой страницы на нашем сайте или удален 404</h1>")
