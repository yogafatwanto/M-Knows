from django import forms
from .models import MlData

class MlDataForm(forms.ModelForm):
    class Meta:
              model = MlData
              fields = "__all__"