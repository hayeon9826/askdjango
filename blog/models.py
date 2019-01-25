from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name


class Post(models.Model):
    writer = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    date = models.DateField()
    likes = models.IntegerField()

    def __str__(self):
        return self.title