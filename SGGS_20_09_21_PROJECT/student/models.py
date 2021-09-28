from django.db import models
from django.forms.fields import ImageField
from django.utils.safestring import mark_safe

class Country(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class City(models.Model):
    Name = models.CharField(max_length=30, default='---')
    Country_field = models.ForeignKey(Country, on_delete=models.CASCADE)
    Population = models.PositiveIntegerField()
    State = models.CharField(max_length=30, default='---')
    field = models.CharField(max_length=30, default='Read only field')
    are_you_Student = models.BooleanField(default=False)
    thumbnail = models.ImageField(upload_to='Images/', null=True, blank=True)

    def image_tag(self):
        return mark_safe('<img src="/../../Static/%s" width="150" height="150" />' % (self.thumbnail))

    image_tag.allow_tags = True

class Percentage(models.Model):
    marks = models.PositiveIntegerField()
    #name = models.CharField(max_length=30)
    #country_field = models.ForeignKey(Country, on_delete=models.CASCADE)
    #population = models.PositiveIntegerField()




