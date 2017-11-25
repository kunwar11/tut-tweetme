from django.db import models
from django.conf import settings
# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)