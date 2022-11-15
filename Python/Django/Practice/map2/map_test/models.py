from django.db import models

# Create your models here.
class Map(models.Model):
    manageNo = models.CharField(max_length=300, blank=True)
    parkNm = models.CharField(max_length=300, blank=True)
    parkSe = models.CharField(max_length=300, blank=True)
    rdnmadr = models.CharField(max_length=300, blank=True)
    lnmadr = models.CharField(max_length=300, blank=True)
    latitude = models.CharField(max_length=300, blank=True)
    longitude = models.CharField(max_length=300, blank=True)
    parkAr = models.CharField(max_length=300, blank=True)
    mvmFclty = models.CharField(max_length=300, blank=True)
    amsmtFclty = models.CharField(max_length=300, blank=True)
    cnvnncFclty = models.CharField(max_length=300, blank=True)
    cltrFclty = models.CharField(max_length=300, blank=True)
    etcFclty = models.CharField(max_length=300, blank=True)
    appnNtfcDate = models.CharField(max_length=300, blank=True)
    institutionNm = models.CharField(max_length=300, blank=True)
    phoneNumber = models.CharField(max_length=300, blank=True)
    referenceDate = models.CharField(max_length=300, blank=True)
    instt_code = models.CharField(max_length=300, blank=True)
    institutionProvide = models.CharField(max_length=300, blank=True)
