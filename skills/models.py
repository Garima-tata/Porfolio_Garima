from django.db import models

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    
    def __str__(self):
        return self.skill_name 
