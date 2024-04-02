from rest_framework import serializers
from .  models import student_data
 

class student_data_serializers(serializers.Serializer):
    students_name = serializers.CharField(max_length=50)
    student_subject = serializers.CharField(max_length=100)
    student_age = serializers.IntegerField()

    #validating

    def create(self, validated_data):
        return student_data.objects.create(**validated_data)