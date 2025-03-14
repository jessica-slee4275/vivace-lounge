from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def promotion(request):
    return render(request, 'promotion.html')

def brow(request):
    return render(request, 'services/brow.html')

def skin(request):
    return render(request, 'services/skin.html')

def smp(request):
    return render(request, 'services/smp.html')

def smp_faq(request):
    return render(request, 'services/smp/faq.html')

def smp_about_smp(request):
    return render(request, 'services/smp/about-smp.html')

def smp_about_smp_psychological_impact(request):
    return render(request, 'services/smp/about-smp/psychological-impact.html')

def smp_about_smp_and_hair_growth(request):
    return render(request, 'services/smp/about-smp/smp-and-hair-growth.html')

def smp_about_smp_last(request):
    return render(request, 'services/smp/about-smp/smp-last.html')

def training(request):
    return render(request, 'training.html')



def contact(request):
    return render(request, 'contact.html')

# def faq(request):
#     return render(request, 'faq.html')

# def services(request):
#     return render(request, 'services.html')

# def smp(request):
#     return render(request, 'services/smp.html')

# def semi_permanent_brows(request):
#     return render(request, 'services/semi_permanent_brows.html')

# def brow_styling(request):
#     return render(request, 'services/brow_styling.html')