from django.db import models
from .utils import unique_code

# Create your models here.
from django.db import models
# Create your models here.
class ModelData(models.Model):
    old_url = models.CharField(max_length=200)
    short_url = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f'Short URL for:  {self.old_url} is {self.short_url}'

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = unique_code(self)
        super().save(*args, **kwargs)

