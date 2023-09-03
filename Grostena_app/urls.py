"""
URL configuration for Grosstena01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('search_results/', views.search_results, name='search_results'),
    path('service_details/<int:service_id>/', views.service_details, name='service_details'),
    path('', views.index, name='index'),
    path('register_service/', views.register_service, name='register_service'),    path('service_form/', views.service_form, name='service_form'),
    path('switch_language/<str:language>/', views.switch_language, name=''),

    path('user_form/', views.user_form, name='user_form'),
    path('login/', views.login_view, name='login'),  # Определение URL для login_view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]
