from django.db import models
#from .category import Category


class Article(models.Model):
    STATUS = (
        (0, "in writing"),
        (1, "pending editor approval"),
        (2, "published"),
    )

    title = models.CharField(max_length=128)
    author = models.CharField(max_length=64, null=True)
    content = models.TextField()
    date_added = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS)
    publish_date = models.DateField(null=True)
    removal_date = models.DateField(null=True)
    categories = models.ManyToManyField("Category")