from django.shortcuts import render
from . forms import MlDataForm
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from . models import MlData
from . serializers import MlDataSerializers
import pickle
import joblib
import json
import numpy as np
from sklearn import preprocessing
import pandas as pd
from sklearn.ensemble import RandomForestClassifier





# class KreditStatus(viewsets.ModelViewSet):
#     queryset = MlData.objects.all()
#     serializers_class = MlDataSerializers

@api_view(["POST"])
def get_kredit_status(request):
    try:
        
        model = joblib.load("/Users/yogafatwanto/Documents/magang/Magang M-Knows/M-Knows/django_deployment/deploy/app/klasifikasi_model.pkl")
        data = request.data
        values = list(data.values())
        
        # Convert values to a NumPy array
        unit = np.array(values).reshape(1, -1)
        
        # Make prediction using the model
        prediction = model.predict(unit)
        
        # Return the prediction in the response
        return Response({"prediction": prediction[0]})
    except Exception as e:
        return Response({"error": str(e)})
