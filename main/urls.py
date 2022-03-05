from django.urls import path
from main.views import main_page,RestApiLight,rest_api_light,UserLoginView


app_name='main'
urlpatterns=[
    path('api/',RestApiLight.as_view(),name='rest_page'),
    path('',main_page,name='main_page'),
    path('api1/',rest_api_light,name='rest_page1'),
    path('login/',UserLoginView.as_view(),name='login_page'),
]