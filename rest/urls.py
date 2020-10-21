
from django.urls import path, include

urlpatterns = [
    path('api/', include('rest.app.user.urls')),
    path('api/', include('rest.app.profile.urls')),
]
