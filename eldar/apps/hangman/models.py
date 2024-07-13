from django.db import models

class Game(models.Model):
    words = models.CharField(max_length=100)
    guessed_word = models.CharField(max_length=100)
    attempts_left = models.IntegerField(default=6)

    def __str__(self):
        return self.words
