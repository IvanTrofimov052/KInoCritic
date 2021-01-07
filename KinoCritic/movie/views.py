from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .service import *


def get_movie_page(request, film_name):
    return JsonResponse(get_information_about_movie_with_comments_and_actors(film_name))
