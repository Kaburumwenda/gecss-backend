from django.db import models

# Create your models here.

class AgentPayment(models.Model):
    agentNo = models.CharField(max_length=20)
    amount = models.PositiveIntegerField(default=1)
    fromDate = models.DateField()
    toDate = models.DateField()
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Paid')

    def __str__(self):
        return self.agentNo