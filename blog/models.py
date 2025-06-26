from django.db import models

# Create your models here.

    

class Box(models.Model):  
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
class BoxImage(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='box_images/')
    details = models.TextField(blank=True)


    def __str__(self):
        return f"Image for {self.box.title}"
    
class Description(models.Model):
    image = models.ImageField()
    heading = models.CharField(max_length=100)
    details = models.TextField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"