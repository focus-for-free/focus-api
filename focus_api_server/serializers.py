from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plan
        fields = ('types', 'content')
