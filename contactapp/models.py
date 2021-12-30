from django.db import models
from django.db.models.query_utils import check_rel_lookup_compatibility

# Create your models here.
class table1(models.Model):
    title=models.CharField(max_length=25, default="")
    fullname=models.CharField(max_length=25, default="")
    position=models.CharField(max_length=25, default="")
    company=models.CharField(max_length=25, default="")
    email=models.CharField(max_length=25, default="")
    saddr1=models.CharField(max_length=25, default="")
    saddr2=models.CharField(max_length=25, default="")
    country=models.CharField(max_length=25, default="")
    city=models.CharField(max_length=25, default="")
    state=models.CharField(max_length=25, default="")
    zip=models.IntegerField(max_length=6, default="")
    phone=models.CharField(max_length=25, default="")
    