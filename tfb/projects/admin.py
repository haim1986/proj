from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Creator)
admin.site.register(Person)
admin.site.register(Movie)
admin.site.register(Feedbaker)
admin.site.register(GivenFeedback)