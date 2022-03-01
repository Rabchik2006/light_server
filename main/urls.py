from django.urls import path
from main.views import main_page,RestApiLight,rest_api_light


app_name='main'
urlpatterns=[
    path('',main_page,name='main_page'),
    path('api/',RestApiLight.as_view(),name='rest_page'),
    path('api1/',rest_api_light,name='rest_page1'),
]