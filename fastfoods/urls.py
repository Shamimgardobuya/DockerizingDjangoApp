from django.urls import path
from fastfoods.views import menu

urlpatterns = [
    path("menu/<str:item>", menu, name="item")
]
