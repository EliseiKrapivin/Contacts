from django.db import models

class Contact(models.Model):
    second_name = models.CharField(max_length=10)
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    photo = models.ImageField(upload_to ='uploads/')
    birthday = models.DateField()

    def __str__(self):
        return self.name