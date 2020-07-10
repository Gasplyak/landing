from django.db import models

class Good(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField(max_length=1000, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    price = models.CharField(max_length=10, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    img = models.ImageField(upload_to='media')

    class Meta:
        verbose_name_plural = 'Goods'

    def __str__(self):
        return self.title


