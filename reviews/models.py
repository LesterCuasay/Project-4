from django.db import models
from django.contrib.auth.models import User
from datetime import date

STATUS = ((0, "Draft"), (1, "Published"))


class BookingReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    email = models.EmailField()
    comment = models.TextField(max_length=350)
    service_rating = models.IntegerField(default=0)
    food_rating = models.IntegerField(default=0)
    overall_rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.author.username
