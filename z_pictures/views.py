from django.shortcuts import render

from .models import Category, Image, Location


# Create your views here.
def home(request):
    all_images = Image.objects.all()
    all_locations = Location.objects.all()
    all_categories = Category.objects.all()
    return render(request, 'all-pictures/home.html', {'all_locations': all_locations, 'all_images': all_images,
                                                      'all_categories': all_categories})


def search(request,):
    return None


def location(request, location):
    all_images = Image.filter_by_location(location)
    return render(request, 'all-pictures/location.html', {'all_images': all_images})
