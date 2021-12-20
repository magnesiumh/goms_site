from django.db import models

# Create your models here.
class Vids(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    Embedded_link = models.CharField(max_length=1000, unique=True)
    Date_taken = models.DateTimeField()
    iclass = models.CharField(max_length=20 )

    


def __str__(self):
    return self.title
