from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70,unique=True)

    def __unicode__(self):              # __unicode__ on Python 2
        return self.first_name

