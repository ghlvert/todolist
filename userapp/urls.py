from django.urls import include, path

from userapp.views import registration
app_name = 'userapp'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration', registration, name='registration')
]