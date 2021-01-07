from django.urls import path

from . import views

urlpatterns = [
	# Ex: movie/Terminator
	path('<str:film_name>/', views.get_movie_page, name=''),
]