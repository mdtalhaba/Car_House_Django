from django.shortcuts import render
from brand.models import Brand
from car.models import Car
from django.views.generic import DetailView

def home(req, brand_slug = None) :
    data = Car.objects.all()
    if brand_slug is not None :
        brd = Brand.objects.get(slug=brand_slug)
        data = Car.objects.filter(brand=brd)
    brand = Brand.objects.all()
    return render(req, 'home.html', {'data' : data, 'brand' : brand})


class DetailsCarView(DetailView) :
    model = Car
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'
        
