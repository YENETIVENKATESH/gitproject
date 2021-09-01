from django.db import models

# Create your models here.


class Recipe(models.Model):

    name = models.CharField(max_length=300)
    ingredients = models.CharField(max_length=1200)
    process = models.CharField(max_length=1500)
    images = models.ImageField(upload_to="images/", null=True, blank=True)
    pub_date = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name


