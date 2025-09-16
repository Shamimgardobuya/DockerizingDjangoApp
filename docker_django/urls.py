from django.urls import path
from .views import docker_lite_message




urlpatterns = [
    path('', docker_lite_message, name="first_view")
]
