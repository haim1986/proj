from django.db import models

# Create your models here.

class Topic(models.Model):
    topName = models.CharField (max_length=256, unique=True)
    def __str__(self):
        return self.topName

class Webpage (models.Model):
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord (models.Model):
    Topic = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

