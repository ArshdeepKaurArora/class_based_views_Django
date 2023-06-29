from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class ReviewsModel(models.Model):
    username = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)])
