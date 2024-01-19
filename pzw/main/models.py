from django.db import models

## Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.name} by {self.surname}"

    
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
        return f"{self.author} by {self.title}"
    
    class Meta:
        unique_together = ('author', 'title')
