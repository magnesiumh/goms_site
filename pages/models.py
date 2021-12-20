from django.db import models


# Create your models here.
class page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    permalink = models.CharField(max_length=12, unique=True)
    update_date = models.DateTimeField('Last Updated')
    bodytext = models.TextField('Page Content', blank=True)


def __str__(self):
    return self.title
