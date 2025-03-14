from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 홈페이지
    path('about/', views.about, name='about'), 
    path('promotion/', views.promotion, name='promotion'), 
    path('brow/', views.brow, name='brow'), 
    path('skin/', views.skin, name='skin'), 
    path('smp/', views.smp, name='smp'), 
    path('smp/faq/', views.smp_faq, name='smp_faq'), 
    path('smp/about-smp/', views.smp_about_smp, name='smp_about_smp'), 
    path('smp/about-smp/psychological-impact', views.smp_about_smp_psychological_impact, name='smp_about_smp_psychological_impact'), 
    path('smp/about-smp/smp-and-hair-growth', views.smp_about_smp_and_hair_growth, name='smp_about_smp_and_hair_growth'), 
    path('smp/about-smp/smp-last', views.smp_about_smp_last, name='smp_about_smp_last'), 
    path('training/', views.training, name='training'),  
    path('contact/', views.contact, name='contact'),  
    
    # path('faq/', views.faq, name='faq'),  
    # path('services/', views.services, name='services'),  
    # path('services/smp/', views.smp, name='smp'),  
    # path('services/brow-styling/', views.brow_styling, name='brow-styling'),  
    # path('services/semi-permanent-brows/', views.semi_permanent_brows, name='semi-permanent-brows'),  
]