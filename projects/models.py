from django.db import models

# Create your models here.
#what u added at the admin page path

class Project(models.Model):
    title = models.CharField(max_length=250)
    project_image = models.ImageField(upload_to='images/')
    description = models.TextField()
    
    def __str__(self):
        return self.title

class Classes(models.Model):
    class_title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(default="null")

    def __str__(self):
        return self.class_title
# ask dad about price and if yes add price felid

class Sword_img(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title


# at a later date have a felid possibly to use for the card for the travel and logins information 
class Hotel(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title

# admin feild for blog posts


class Blog(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title
