from django.db import models


class Phone(models.Model):

    name = models.TextField(null=False, blank=False, unique=True)
    price = models.IntegerField()
    image = models.TextField(null=False, blank=False, unique=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.id} - {self.name} - {self.price} - {self.release_date} - {self.slug}'

