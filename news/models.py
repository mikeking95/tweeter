from django.db import models

# Create your models here.
class Headline(models.Model):
    # source, author, title, description, url, urlToImage, publishedAt, content
    source = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    urlToImage = models.URLField(blank=True, null=True)
    publishedAt = models.DateTimeField(auto_now_add=False)
    content = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
