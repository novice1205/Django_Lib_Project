from django.contrib import admin
from django.urls import path, include
from ARSDLib import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name="home"),
    path('about/', views.about, name="about"),
    path('membership/', views.membership, name= "membership")
]
