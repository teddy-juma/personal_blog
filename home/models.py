from django.db import models

# Create your models here.

class Post(models.Model):
    post_title = models.CharField(max_length=130)
    date = models.DateField()
    author = models.CharField(max_length=20)
    image = models.BinaryField(blank=True)
    content = models.TextField()
