from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .band import Band


class Album(models.Model):
    STARS = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )

    title = models.CharField(max_length=100)
    release_year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2100)])
    rating = models.IntegerField(choices=STARS)
    band = models.ForeignKey(Band, on_delete=models.CASCADE)