from django.db import models
import datetime as dt


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

