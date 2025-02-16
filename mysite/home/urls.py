from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 홈페이지
    path('about/', views.about, name='about'), 
    path('services/', views.services, name='services'),  
    path('services/smp', views.smp, name='smp'),  
    path('contact/', views.contact, name='contact'),  
]