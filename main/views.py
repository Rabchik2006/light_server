from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render,HttpResponse
import json,os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


if os.environ.get('GPIO_EXIST'):
    import RPi.GPIO as GP
    pin = int(os.environ.get('LIGHT_PIN'))
    GP.setmode(GP.BCM)
    GP.setup(pin,GP.OUT)
else:
    import repl_gp as GP
    pin='None'

@login_required(login_url='/login/')
def main_page(request):
    with open('data.json','r') as f:
        old_data=json.load(f)
    context={'old_data':old_data}
    if request.method=='POST':
        print(request.POST)
        unf_data=dict(request.POST)

        print(unf_data)
        context.update({'data':unf_data})
        if unf_data['hour']!=None and unf_data['minute']!=None:
            data={'hour':int(unf_data['hour'][0]),'minute':int(unf_data['minute'][0])}
            if data.get('condition'):
                data['condition']=1
            else:
                data['condition']=0
            with open('data.json','w') as f:
                json.dump(data,f,indent=4)
    return render(request,'main.html')


class RestApiLight(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # print(request.data)
        GP.output(pin,request.data['state'])
        return Response('hello')

@api_view(http_method_names=['POST'])
def rest_api_light(request):
    if request.method=="POST":
        print(request.data)
    return Response('hello')


class UserLoginView(LoginView):
    template_name = 'login.html'
    next_page = '/'