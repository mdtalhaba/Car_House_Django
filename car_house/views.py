from django.shortcuts import render, redirect
from brand.models import Brand
from car.models import Car
from django.views.generic import DetailView
from car.forms import CommentForm
from django.urls import reverse
from transection.models import Transection
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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

    def post(self, request, *args, **kwargs) :
        comment_form = CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid() :
            new_comment = comment_form.save(commit=False)
            new_comment.post = car
            new_comment.save()
            new_comment = ''
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = CommentForm()
            
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
def buy_car(req, car_id):
    car = Car.objects.get(id=car_id)
    if car.quantity > 0:
        transection = Transection(user=req.user, car_id=car_id, quantity=1)
        transection.save()
        car.quantity -= 1
        car.save()
        current_url = reverse('car_details', args=[car_id])
        return redirect(current_url)

        
