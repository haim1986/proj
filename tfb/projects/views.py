from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *

def index(request):
    all_movies = Movie.objects.all()
    context = {'all_movies' : all_movies}
    return render(request, 'projects/index.html', context)

def moviesDetails(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    givenFeedbacks = get_list_or_404(GivenFeedback, movie_id=movie_id)
    return render(request, 'projects/detail.html', {"movie":movie, "givenFeedbacks":givenFeedbacks})

def favorite(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    givenFeedbacks = get_list_or_404(GivenFeedback, movie_id=movie_id)
    try:
        selected_fdbker = movie.givenFeedback_set.get(pk=request.POST['fdbk'])
    except (KeyError):
        return render(request, 'projects/detail.html', {"movie": movie, "givenFeedbacks": givenFeedbacks})

    else:
        selected_fdbker.is_favorite = True
        selected_fdbker.save()
        return render(request, 'projects/detail.html', {"movie": movie, "givenFeedbacks": givenFeedbacks})





