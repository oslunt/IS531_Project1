from django.db import models

# Create your models here.

class DonutInfo(models.Model):
    donut_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'donut_info'
    def __str__(self):
        return self.name