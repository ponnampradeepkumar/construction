"""
URL configuration for gkconstructions project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from work import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.work_progress_create, name='work_progress_create'),
    path('Details_table', views.work_progress_list, name='work_progress_list'),
    path('ok/', views.ok, name='ok'),
    path('index/', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),

    path('data/<int:data_id>/', views.site_details, name='site_details'),


    path('login/', views.login_view, name='login'),




 path('contract_deal_list', views.contact_deal_list, name='contact_deal_list'),
    path('contract_deal_form/', views.contact_deal_create, name='contact_deal_create'),
    path('edit/<int:pk>/', views.contact_deal_edit, name='contact_deal_edit'),
    path('detail/<int:pk>/', views.contact_deal_detail, name='contact_deal_detail'),









   
]


  
  
  
    


