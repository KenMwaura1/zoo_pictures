from django.shortcuts import render



# Create your views here.
def home(request):
    return render(request, 'all-pictures/home.html')


def search(request):
    return None


def location(request):
    return None