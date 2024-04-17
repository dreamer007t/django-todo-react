from django.db import models

# Create your models here.
class Message(models.Model):
    email = models.EmailField()
    text = models.TextField()

    def __str__(self) :
        return self.email