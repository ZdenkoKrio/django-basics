from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=128)
    duration = models.TimeField(null=True)
    album = models.ForeignKey("Album", on_delete=models.CASCADE)
