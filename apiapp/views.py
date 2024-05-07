from django.shortcuts import render
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import ApiTestModel

def index(request):
    q = ApiTestModel.objects.all()
    data = serialize('json',q,fields=('id','title'))
    return HttpResponse(data,content_type='application/json')
