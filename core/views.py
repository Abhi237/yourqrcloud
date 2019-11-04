from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime

x = datetime.datetime.now()
import json

def home(request):
    return render(request,'core/home.html')

def clip(request):
    key=request.POST.get("key")
        
    data=json.load(open('core/data.json','r',encoding='utf-8'))
    if key[:2] in data and key[2:]==x.strftime('%d%m%y'):
        finaldata=data[key[:2]]
    elif key[:2]=="xx":return redirect("https://prepinsta.com/elite/")
    else:finaldata=data['item']
    context={
        "renderdata":finaldata
    }
    return render(request,'core/yourclipboard.html',context)