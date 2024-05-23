from django.db import models

# Create your models here.
class ckdModel(models.Model):

    Albumin=models.FloatField()
    Blood_Glucose_Random=models.FloatField()
    Blood_Urea=models.FloatField()
    Serum_Creatine=models.FloatField()
    Packed_cell_volume=models.FloatField()
    White_blood_count=models.FloatField()

def __str__(self):
        return f"{self.Albumin}, {self.Blood_Glucose_Random}, {self.Blood_Urea}, {self.Serum_Creatine}, {self.Packed_cell_volume}, {self.White_blood_count}"