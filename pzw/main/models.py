from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

## Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    # image = models.ImageField(upload_to='main/static/main/images/')

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        unique_together = ('name', 'surname')
    
class Genre(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    genres = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, default=0, on_delete=models.CASCADE)
    title = models.CharField(max_length=159)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} By: {self.author}"
    
    class Meta:
        unique_together = ('author', 'title')

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.OneToOneField(Book, on_delete=models.CASCADE, primary_key=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1, message="Najmanja ocijena je 1."),
            MaxValueValidator(10, message="Najveća ocijena je 10."),
        ]
    )