from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 홈페이지
    path('about/', views.about, name='about'), 
    path('services/', views.services, name='services'),  
    path('services/smp', views.smp, name='smp'),  
    path('services/brow-styling', views.brow_styling, name='brow-styling'),  
    path('services/semi-permanent-brows', views.semi_permanent_brows, name='semi-permanent-brows'),  
    path('contact/', views.contact, name='contact'),  
]