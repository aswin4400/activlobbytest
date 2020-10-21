
from rest_framework import status
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest.app.user.serializers import UserRegistrationSerializer
from rest.app.profile.models import UserProfile
from rest.app.user.models import User
from .env import *
import requests
class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = UserProfile.objects.get(user=request.user)
            user_profiles = User.objects.filter(parent=request.user)
            user_profiles= list(user_profiles.values())
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                
                'data': [{
                    'first_name': user_profile.first_name,
                    'last_name': user_profile.last_name,
                    'phone_number': user_profile.phone_number,
                    'age': user_profile.age,
                    'gender': user_profile.gender,
                    'id':request.user.id
                    },{'users':user_profiles}]
                
                }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)

class WeatherView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    
    def options(self, request):
        console.log("hello")
        allowed_methods = ['get', 'post', 'put', 'delete', 'options']
        response = HttpResponse()
        response['allow'] = ','.join([allowed_methods])
        return response

    def get(self,request):
        # base URL
        BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
        # City Name CITY = "Hyderabad"
        # API key API_KEY = "Your API Key"
        # upadting the URL
        URL = BASE_URL + "q=" + 'Kochi' + "&appid=" + API_KEY
        # HTTP request
        response = requests.get(URL)
        status_code =response.status_code
        # checking the status code of the request
        if response.status_code == 200:
        # getting data in the json format
            data = response.json()
            # getting the main dict block
            main = data['main']
            # getting temperature
            temperature = main['temp']
            # getting the humidity
            humidity = main['humidity']
            # getting the pressure
            pressure = main['pressure']
            # weather report
            report = data['weather']

            response = {
                         'success': 'true',
                         'status code': status_code,
                         'message': 'Weather Fetched',
                        'data': [{
                            'temperature': temperature,
                            'humidity': humidity,
                            'pressure': pressure,
                            'weather_report': report[0]['description'],
                            }]
            }
            return Response(response, status=status_code)
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'Somthing Fishy',
                }
            return Response(response, status=status_code)