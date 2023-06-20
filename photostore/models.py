from django.db import models

# Create your models here.

class Caption(models.Model):
    title = models.CharField(max_length=200)
    continent = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    imageID = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)


    def __str__(self):
        return f'{self.title}'
    
    # this will order the books by date created
    class Meta:
        ordering = ['-date_created']




