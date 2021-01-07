from .models import Movie


def get_information_about_movie_with_comments_and_actors(movie_name):
	responce = {}

	responce['information about film'] = get_information_about_movie(movie_name)

	return responce


def get_information_about_movie(movie_name):
	responce = {}

	movie = Movie.objects.get(movie_name=movie_name)

	responce['film_name'] = movie.movie_name
	responce['image_url'] = movie.image_url
	responce['trailer_link'] = movie.trailer_link
	responce['description'] = movie.description
	responce['raiting'] = movie.raiting

	return responce