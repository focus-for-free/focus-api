from django.shortcuts import render
from rest_framework import viewsets

from .serializers import PlanSerializer
from .models import Plan

class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer

