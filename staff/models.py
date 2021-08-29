from django.db import models


class Staff(models.Model):
    title = models.CharField(max_length=75)
    content = models.TextField(max_length=255, blank=True)
    contact_url = models.URLField
    photo = models.ImageField(upload_to='photo/%Y/%m')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
