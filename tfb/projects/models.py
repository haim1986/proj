from __future__ import unicode_literals
from django.db import models



class Person(models.Model):
    #ID = models.AutoField()
    user_name = models.CharField(max_length=400)
    age = models.IntegerField()
    country = models.CharField(max_length=80)
    gender = models.CharField(max_length=1)
    feedbacker = models.BooleanField()
    isCreator = models.BooleanField()
    def __str__(self):
        return self.user_name

class Creator(models.Model):
    Creators_ID = models.ForeignKey(Person, on_delete=models.CASCADE,)
    imdb_link = models.URLField()
    def __str__(self):
        return self.Creators_ID.user_name

class Movie(models.Model):
    #movie_ID = models.AutoField()
    name = models.CharField(max_length=400)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    year = models.IntegerField()
    genre = models.CharField(max_length=20)
    link_to_review_page = models.URLField(default="there is no link")
    # language = models.CharField(max_length=400)
    # synopsis = models.TextField(max_length=1000)
    # length = models.DurationField()
    # link_to_the_movie = models.URLField()
    # poster = models.URLField()
    # uploade_date = models.DateField()
    def __str__(self):
        return self.name

class Feedbaker(models.Model):
    feedbacker_name = models.ForeignKey(Person, on_delete=models.CASCADE)
    money_earn = models.IntegerField()
    profession = models.CharField(max_length=400)
    vested_money_to_withdrow = models.IntegerField()
    feedback_avg_rate = models.IntegerField() #todo: verify protection
    num_of_feedbacks_he_gave = models.IntegerField()
    def __str__(self):
        return self.feedbacker_name.user_name

class GivenFeedback(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    feedbacker_name = models.ForeignKey(Feedbaker, on_delete=models.CASCADE)
    rate = models.IntegerField( 'rate by creator', blank=True, null=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return str(self.movie_id.name) +" - " + str(self.feedbacker_name.feedbacker_name)







