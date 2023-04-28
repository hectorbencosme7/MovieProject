from django.db import models

# Create your models here.


class movieData(models.Model):

    def __str__(self):      #This line makes the item in admin panel
        return self.name    #display the name and not 'object'
       

    name = models.CharField(max_length=200)
    duration=models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='images/',default="images/noimage.png")