from django.db import models

# Create your models here.
from django.db import models

class Drug(models.Model):
    drug_id = models.AutoField(primary_key=True)  # Auto increment ID
    drug_name = models.CharField(max_length=100)  # Name of the drug
    category = models.CharField(max_length=100)   # Drug category (e.g., Antibiotic, Painkiller, etc.)
    dosage = models.CharField(max_length=50)      # Dosage (e.g., 500mg, 10ml, etc.)
    manufacturer = models.CharField(max_length=100) # Manufacturer's name
    batch_no = models.CharField(max_length=50)    # Batch number
    expiry_date = models.DateField()              # Expiry date of the drug
    stock = models.IntegerField()                 # Number of units in stock

    def __str__(self):
        return f"{self.drug_name} - {self.drug_id}"

class Consumption(models.Model):
    drug = models.ForeignKey(Drug, on_delete=models.CASCADE)
    date = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} units of {self.drug.name} on {self.date}"