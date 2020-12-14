from django.urls import path, include
from users import views
from users.views import CustomAuthToken

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
    path('api-token-auth/', CustomAuthToken.as_view())
]
