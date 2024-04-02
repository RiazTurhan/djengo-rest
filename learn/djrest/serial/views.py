from django.shortcuts import render
from serial.models import student_data
from serial.serializers import student_data_serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt 
import io
from django.db import transaction
from rest_framework.parsers import JSONParser
import json
from . import serializers


#we create queryset for views
# Create your views here.

def student_info(request):
    #complex data 🔽

    student_Complex_data = student_data.objects.all()

    # complex data to python dic
    
    serializer = student_data_serializers( student_Complex_data, many = True)

    #render json()

    json_data = JSONRenderer().render(serializer.data)

    #json() send to user
    return HttpResponse(json_data, content_type = 'application/json')



@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body

        #covert stream

        stream = io.BytesIO(json_data)
        #stream to python

        python_data = JSONParser().parse(stream)

        #python to complex

        srializer = serializers.student_data_serializers(data=python_data)
        if srializer.is_valid():
            srializer.save()
            result = {'msg': 'succesfully complete'}
            json_data = JSONRenderer().render(result)
            return HttpResponse (json_data , content_type = 'application.json')
        json_data = JSONRenderer().render(srializer.errors)
        return HttpResponse (json_data , content_type = 'application.json')