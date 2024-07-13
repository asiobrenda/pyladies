from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta:
        verbose_name_plural='Post'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title

