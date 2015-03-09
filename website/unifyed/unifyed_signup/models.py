from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
                  
    def __unicode__(self):
        return "{0} {1} {2} {3}".format(
            self, self.first_name, self.last_name, self.email)

