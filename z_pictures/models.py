from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        return Location.objects.all()

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(name=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=45)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    def __str__(self):
        return self.name


# Create your models here.
class Image(models.Model):
    name = models.CharField(max_length=65)
    description = models.TextField()
    author = models.CharField(max_length=43, default='admin')
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        ordering = ['date']

    @classmethod
    def get_image_by_id(cls, id):
        return cls.objects.filter(id=id).all()

    @classmethod
    def filter_by_location(cls, location):
        return Image.objects.filter(location__name=location).all()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def search_by_category(cls, category):
        return cls.objects.filter(category__name__icontains=category)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def __str__(self):
        return self.name
