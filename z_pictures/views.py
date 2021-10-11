from django.shortcuts import render

from .models import Category, Image, Location


# Create your views here.
def home(request):
    all_images = Image.objects.all()
    all_locations = Location.objects.all()
    all_categories = Category.objects.all()
    print(all_locations)
    return render(request, 'all-pictures/home.html', {'all_locations': all_locations, 'all_images': all_images,
                                                      'all_categories': all_categories})


def search(request):
    if 'search' in request.GET and request.GET['search']:
        category = request.GET.get("search")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request, 'all-pictures/search_results.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'all-pictures/search_results.html', {"message": message})


def location(request, location):
    all_images = Image.filter_by_location(location)
    print(location)

    print(all_images)
    return render(request, 'all-pictures/location.html', {'all_images': all_images, 'location': location})
