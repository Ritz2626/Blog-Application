from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    description=HTMLField()
    date1=models.DateField(null=True)
    cover_photo=models.ImageField(null=True, blank=True ,upload_to = 'cover')
   
   
    def __str__(self):
        return self.title +"|"+str(self.author)
        
