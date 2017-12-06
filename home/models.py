from django.db import models

# Create your models here.

class Authors(models.Model):
    author_name = models.CharField(max_length=50)
    author_email = models.CharField(max_length=30)

    def __str__(self):
        return self.author_name
    
class Post(models.Model):
    post_title = models.CharField(max_length=130)
    date = models.DateField()
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    image = models.BinaryField(blank=True)
    content = models.TextField()

    def __str__(self):
        return self.post_title
