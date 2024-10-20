from django.db import models

# Create your models here.

class RepairRequest(models.Model):
    device_name = models.CharField(max_length=255)
    description_problem = models.TextField()
    preferred_date_time_repair = models.DateTimeField()
    contact_info = models.CharField(max_length=255)

    def __str__(self):
        return self.device_name
