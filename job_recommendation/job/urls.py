from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/',admin.site.urls),
    path("",views.job, name="job"),
    path("result/<str:location>/<str:keywords>/",views.result, name="result"),   
]