from django.shortcuts import render
from .models import Film
def add_film(request):
    data = {
        'caption': "New"
    }
    return render(request, 'films/add_film.html', data)


def film_list(request):
    films = Film.objects.all()
    return render(request, 'films/film_list.html', {'films': films})
