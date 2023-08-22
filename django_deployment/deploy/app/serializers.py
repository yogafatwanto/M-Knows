from rest_framework import serializers 
from .models import MlData 

class MlDataSerializers(serializers.ModelSerializer): 
    class meta: 
        model=MlData 
        fields='__all__'