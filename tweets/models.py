from django.db import models

class Tweet(models.Model):
    # id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    published_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content