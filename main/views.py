from django.shortcuts import render,HttpResponse
from main.forms import TimeForm
import json,os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

import RPi.GPIO



GP.setmode(GP.BCM)
pin=int(os.environ.get('LIGHT_PIN'))
GP.setup(pin,GP.OUT)

def main_page(request):
    form=TimeForm()
    with open('data.json','r') as f:
        old_data=json.load(f)
    context={'form':form,'old_data':old_data}
    if request.method=='POST':
        print(request.POST)
        if request.POST.get('hour',None)!=None:
            form=TimeForm(request.POST)
            if form.is_valid():
                data=form.cleaned_data
                print(data)
                context.update({'data':data})
                if data['hour']!=None and data['minute']!=None and (data['condition']=='on' or data['condition']=='off'):
                    with open('data.json','w') as f:
                        json.dump(data,f,indent=4)
            context.update({'form': form})
        else:
            if request.POST.get('switch',None)!=None:
                GP.output(pin,1)
                pass
            else:
                GP.output(pin,0)
                pass
    return render(request,'main.html',context)


class RestApiLight(APIView):
    def post(self, request):
        print(request.data)
        GP.output(pin,request.data['state'])
        return Response('hello')

@api_view(http_method_names=['POST'])
def rest_api_light(request):
    if request.method=="POST":
        print(request.data)
    return Response('hello')