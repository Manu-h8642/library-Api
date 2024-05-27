from django.shortcuts import render
from libapp.models import bdb
from libapp.serializers import serialb
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt

def libapi(request):
    if request.method == "GET":
        x=bdb.objects.all()
        obj = serialb(x,many=True)
        return JsonResponse(obj.data,safe=False)
    elif request.method == "POST":
        x=JSONParser().parse(request)
        obj = serialb(data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data saved successfully...!",safe=False)
        return JsonResponse("invalid data.!",safe=False)
    elif request.method == "PUT":
        x=JSONParser().parse(request)
        y=bdb.objects.get(bid=x['bid'])
        obj = serialb(y,data=x)
        if obj.is_valid():
            obj.save()
            return JsonResponse("Data Updated..!",safe=False)
        return JsonResponse("Faild to update..!",safe=False)
    elif request.method=="DELETE":
        x=bdb.objects.get(bid=id)
        x.delete()
        return JsonResponse("Data Deleted..!", safe=False)