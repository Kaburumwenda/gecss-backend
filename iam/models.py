from django.db import models

# Create your models here.
class Notifications(models.Model):
    STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    title = models.CharField(max_length=250)
    message = models.TextField(max_length=550)
    status = models.CharField(max_length=30, choices=STATUS, default='Active')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title