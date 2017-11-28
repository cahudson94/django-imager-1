"""Define the Photo and Album model classes."""

from django.db import models
from django.contrib.auth.models import User


PUBLISH = (
    ('Private', 'Private'),
    ('Shared', 'Shared'),
    ('Public', 'Public')
)


class Photo(models.Model):
    """Define the Photo class."""

    title = models.CharField(
        max_length=50)
    img = models.ImageField(upload_to='images')
    description = models.CharField(
        max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
    published = models.CharField(
        choices=PUBLISH,
        max_length=10
    )
    user = models.ForeignKey(
        User,
        related_name='photo'
    )


class Album(models.Model):
    """Define the Album class."""

    photos = models.ManyToManyField(Photo, related_name='album')
    title = models.CharField(
        max_length=50, unique=True)
    description = models.CharField(
        max_length=200)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(auto_now_add=True)
    published = models.CharField(
        choices=PUBLISH,
        max_length=10
    )
    cover = models.CharField(
        max_length=50
    )
    user = models.ForeignKey(
        User,
        related_name='album'
    )
