from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile/', default='profile/default.jpg')

    def __str__(self):
        return self.name