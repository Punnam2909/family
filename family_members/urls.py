from django.urls import path,include
from .views import *


urlpatterns = [
    path("FamilyApp/",FamilyApp,name="FamilyApp"),
    path("punnam/", Punnam, name="Punnam"),
    path("ramala/", Ramala, name="Ramala"),
]