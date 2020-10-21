

from django.conf.urls import url
from rest.app.profile.views import UserProfileView,WeatherView


urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    url(r'^weather',WeatherView.as_view())
    ]
