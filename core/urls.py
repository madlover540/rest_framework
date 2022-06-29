"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.db import router
from django.urls import path, include
from reseve import views
from rest_framework.views import APIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('c', views.viewsets_customer)
router.register('s', views.viewsets_saloon)
router.register('r', views.viewsets_Reserve)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('d/', views.no_rest_no_model),
    path('c/', views.no_rest_but_model),
    path('m/', views.fbv_list),
    path('n/<int:pk>/', views.fbv_pk),
    path('h/', views.CBV_list.as_view()),
    path('h/<int:pk>/', views.Cbv_pk.as_view()),
    path('j/', views.mixins_list.as_view()),
    path('j/<int:pk>/', views.mixins_pk.as_view()),
    path('k/', views.generics_list.as_view()),
    path('k/<int:pk>/', views.generics_pk.as_view()),
    path('viewset/', include(router.urls)),
    

]
