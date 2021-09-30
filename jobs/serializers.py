from django.db.models import fields
from rest_framework import serializers
from .models import Job

class JobGetOutputSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ("title")
