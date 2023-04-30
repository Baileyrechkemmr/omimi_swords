from django.db import models

# Create your models here.
#what u addd at the admin page path

class Project(models.Model):
    title = models.CharField(max_length=250)
    project_image = models.ImageField(upload_to='images/')
    discription = models.TextField()
    