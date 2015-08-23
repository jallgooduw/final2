from django import forms

from .models import Device

class DeviceForm(forms.ModelForm):

    class Meta:
        model = Device
        fields = ('productManager',
                    'oem',
                    'dev_CodeName',
                    'dev_MarketName',
                    'dev_OS',
                    'dev_Category',
                    'dev_Class',
                    'spe_LE',
                    'spe_FE',
                    'spe_IFW',
                    'spe_FFW',
                    'spe_TA',
                    'dpm_PR',
                    'dpm_ComSo',
                    'dpm_PreSale',
                    'dpm_GA',
                    'dpm_Cost',
                    'dpm_SRP',
                    'rfp_ScreenSizeW',
                    'rfp_ScreenSizeH',
                    'rfp_ResolutionH',
                    'rfp_ResolutionW',
                    'rfp_Bands',
                    'rfp_CASupport',
                    'rfp_USBType',
                    'rfp_Battery',
                  )