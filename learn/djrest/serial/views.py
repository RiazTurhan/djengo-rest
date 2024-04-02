from django.shortcuts import render
from serial.models import student_data
from serial.serializers import student_data_serializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse



#we create queryset for views
# Create your views here.

def student_info(request, pk):
    #complex data 🔽

    student_Complex_data = student_data.objects.get(id=pk)

    # complex data to python dic
    
    serializer = student_data_serializers( student_Complex_data)

    #render json()

    json_data = JSONRenderer().render(serializer.data)

    #json() send to user
    return HttpResponse(json_data, content_type = 'application/json')

