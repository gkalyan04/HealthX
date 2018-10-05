from django.shortcuts import render
from django.http import HttpResponse
from home.models import Hospital
from django.core import serializers
# Create your views here.

def index(request):
    json_serializer = serializers.get_serializer("json")()
    query_results = json_serializer.serialize( Hospital.objects.all(), ensure_ascii=False )
    data={'query_results':query_results}
    return render(request,'home/index.html',data)
