from django.db import models

class Contactme(models.Model):
    first_name= models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    body=models.CharField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.subject
