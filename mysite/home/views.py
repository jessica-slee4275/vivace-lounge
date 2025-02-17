from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def smp(request):
    return render(request, 'services/smp.html')

def semi_permanent_brows(request):
    return render(request, 'services/semi_permanent_brows.html')

def brow_styling(request):
    return render(request, 'services/brow_styling.html')

def training(request):
    return render(request, 'training.html')

def faq(request):
    return render(request, 'faq.html')

def contact(request):
    return render(request, 'contact.html')