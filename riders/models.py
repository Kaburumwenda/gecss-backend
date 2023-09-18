from django.db import models
import uuid
#pip install uuid uuidfield

# Create your models here.
class Riders(models.Model):
    rider_id = models.UUIDField( unique=True, default=uuid.uuid4, editable=False)
    bike_no = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, default='N/A')
    mobile = models.CharField(max_length=20, default='0700****00')
    alt_mobile = models.CharField(max_length=20, default='0700****00')
    gender = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    id_no = models.CharField(max_length=100)
    id_type = models.CharField(max_length=100)
    date_registered = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='Active')
    is_delete = models.CharField(max_length=2, default='0')
    createdAt = models.DateTimeField(auto_now=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}"
    
    def ID_document_number(self):
        return f"{self.id_no}"
    
    def ID_document_type(self):
        return f"{self.id_type}"