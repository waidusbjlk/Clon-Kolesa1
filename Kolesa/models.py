from django.db import models

class Kolesa(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(update_to="photos/%Y%m/%d")
    time_create = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

