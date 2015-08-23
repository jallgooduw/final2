
from django.forms import widgets
from rest_framework import serializers
from oemfinal.models import Device, OEM_SELECT, OS_SELECT, CA_SELECT, USB_SELECT

class DevicesSerializer(serializers.ModelSerializer):
        class Meta:
                model = Device
                fields = ('id', 'productManager', 'lastSave', 'oem', 'dev_CodeName', 'dev_MarketName', 'dev_OS', 'dev_Category', 'dev_Class', 'spe_LE', 'spe_FE', 'spe_IFW', 'spe_FFW', 'spe_TA', 'dpm_PR', 'dpm_ComSo', 'dpm_PreSale', 'dpm_GA', 'dpm_Cost', 'dpm_SRP', 'rfp_ScreenSizeW', 'rfp_ScreenSizeH', 'rfp_ResolutionH', 'rfp_ResolutionW', 'rfp_Bands', 'rfp_CASupport', 'rfp_USBType', 'rfp_Battery')

def create(self, validated_data):
    return Device.objects.create(**validated_data)

def update(self, instance, validated_data):
    instance.productManager = validated_data.get('productManager', instance.productManager)
    instance.lastSave = validated_data.get('lastSave', instance.lastSave)
    instance.oem = validated_data.get('oem', instance.oem)
    instance.dev_CodeName = validated_data.get('dev_CodeName', instance.dev_CodeName)
    instance.dev_MarketName = validated_data('dev_MarketName', instance.dev_MarketName)
    instance.dev_OS = validated_data('dev_OS', instance.dev_OS)
    instance.dev_Category = validated_data('dev_Category', instance.dev_Category)
    instance.dev_Class = validated_data('dev_Class', instance.dev_Class)
    instance.spe_LE = validated_data('spe_LE', instance.spe_LE)
    instance.spe_FE = validated_data('spe_FE', instance.spe_FE)
    instance.spe_IFW = validated_data('spe_IFW', instance.spe_IFW)
    instance.spe_FFW = validated_data('spe_FFW', instance.spe_FFW)
    instance.spe_TA = validated_data('spe_TA', instance.spe_TA)
    instance.dpm_PR = validated_data('dpm_PR', instance.dpm_PR)
    instance.dpm_ComSo = validated_data('dpm_ComSo', instance.dpm_ComSo)
    instance.dpm_PreSale = validated_data('dpm_PreSale', instance.dpm_PreSale)
    instance.dpm_GA = validated_data('dpm_GA', instance.dpm_GA)
    instance.dpm_Cost = validated_data('dpm_Cost', instance.dpm_Cost)
    instance.dpm_SRP = validated_data('dpm_SRP', instance.dpm_SRP)
    instance.rfp_ScreenSizeW = validated_data('rfp_ScreenSizeW', instance.rfp_ScreenSizeW)
    instance.rfp_ScreenSizeH = validated_data('rfp_ScreenSizeH', instance.rfp_ScreenSizeH)
    instance.rfp_ResolutionH = validated_data('rfp_ResolutionH', instance.rfp_ResolutionH)
    instance.rfp_ResolutionW = validated_data('rfp_ResolutionW', instance.rfp_ResolutionW)
    instance.rfp_Bands= validated_data('rfp_Bands', instance.rfp_Bands)
    instance.rfp_CASupport = validated_data('rfp_CASupport', instance.rfp_CASupport)
    instance.rfp_USBType = validated_data('rfp_USBType', instance.rfp_USBType)
    instance.rfp_Battery = validated_data('rfp_Battery', instance.rfp_Battery) #measure in MaH!
    return instance