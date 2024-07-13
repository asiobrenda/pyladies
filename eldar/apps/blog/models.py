from django.db import models


class Languages(models.Model):
    lang_name = models.CharField(max_length=30)

    def __str__(self):
        return self.lang_name

class Topic(models.Model):
    title = models.CharField(max_length=30)
    text = models.TextField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    lang = models.ForeignKey(Languages, null=True,  on_delete=models.CASCADE, related_name='topic')

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.ForeignKey(Topic, null=True, on_delete=models.CASCADE, related_name='news_title')
    image = models.ImageField(upload_to='blog/')
    text = models.TextField(max_length=5000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)


class Comments(models.Model):
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(News, null=True, on_delete=models.CASCADE, related_name='news_title')

    def __str__(self):
        return str(self.name)