from django.db import models
from django.utils import timezone

# Create your models here.
OEM_SELECT = (
        ('SAMSUNG','SAMSUNG'),
        ('HTC','HTC'),
        ('LG','LG'),
        ('ASUS','ASUS'),
        ('BLACKBERRY','BLACKBERRY'),
        ('HUAWEI','HUAWEI'),
        ('APPLE','APPLE'),
        ('MOTOROLA','MOTOROLA'),
        ('ZTE','ZTE'),
        ('NOKIA','NOKIA'),
        ('MICROSOFT','MICROSOFT'),
        ('PANASONIC','PANASONIC'),
    )

OS_SELECT = (
        ('Android','Android'),
        ('RIM','RIM'),
        ('iOS','iOS'),
        ('Custom','Custom'),
        ('Windows','Windows'),
    )

CA_SELECT =(
        ('YES','YES'),
        ('NO','NO'),
        ('TBD','TBD'),
    )
USB_SELECT=(
        ('Mini','Mini'),
        ('Micro','Micro'),
        ('C','C'),
        ('Proprietary','Proprietary'),
    )

class Device(models.Model):
        productManager = models.ForeignKey('auth.User')
        lastSave = models.DateField(auto_now=True)
        oem = models.CharField(max_length=10, choices=OEM_SELECT)
        dev_CodeName = models.CharField(max_length=200)
        dev_MarketName = models.CharField(max_length=200, blank=True, null=True,)
        dev_OS = models.CharField(max_length=100, choices=OS_SELECT)
        dev_Category = models.CharField(max_length=200, blank=True, null=True,)
        dev_Class = models.CharField(max_length=200, blank=True, null=True,)
        spe_LE = models.DateField(blank=True, null=True,)
        spe_FE = models.DateField(blank=True, null=True,)
        spe_IFW = models.DateField(blank=True, null=True,)
        spe_FFW = models.DateField(blank=True, null=True,)
        spe_TA = models.DateField(blank=True, null=True,)
        dpm_PR = models.DateField(blank=True, null=True,)
        dpm_ComSo = models.DateField(blank=True, null=True,)
        dpm_PreSale = models.DateField(blank=True, null=True,)
        dpm_GA = models.DateField(blank=True, null=True,)
        dpm_Cost = models.FloatField(blank=True, null=True,)
        dpm_SRP = models.FloatField(blank=True, null=True,)
        rfp_ScreenSizeW = models.FloatField(blank=True, null=True,)
        rfp_ScreenSizeH = models.FloatField(blank=True, null=True,)
        rfp_ResolutionH = models.FloatField(blank=True, null=True,)
        rfp_ResolutionW = models.FloatField(blank=True, null=True,)
        rfp_Bands=models.CharField(max_length=200, blank=True, null=True,)
        rfp_CASupport = models.CharField(max_length=10, choices=CA_SELECT, blank=True, null=True,)
        rfp_USBType = models.CharField(max_length=10, choices=USB_SELECT, blank=True, null=True,)
        rfp_Battery = models.FloatField(blank=True, null=True,) #measure in MaH!

	def __str__(self):
		return self.dev_CodeName