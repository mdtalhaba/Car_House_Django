from django.shortcuts import render, redirect
from . forms import SignUpForm, ChangeUserForm, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from transection.models import Transection
from car.models import Car


class UserSignUpView(CreateView) :
    model = User
    form_class = SignUpForm
    template_name = 'user/login_signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Registration Successfull')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Register'
        return context
    

@login_required(login_url="/user/login/")
def update_profile(req) :
    if req.method == 'POST' :
        update_form = ChangeUserForm(req.POST, instance=req.user)
        if update_form.is_valid() :
            messages.success(req, 'Your Information is Successfully Changed')
            update_form.save()
            return redirect('profile')
    else : 
        update_form = ChangeUserForm(instance=req.user)
    return render(req, 'user/login_signup.html', {'form' : update_form, 'type' : 'Update Profile'})
    

class UserLoginView(LoginView) :
    template_name = 'user/login_signup.html'
    
    def get_success_url(self):
        return reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, 'Log In Successfull')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'Log In Information is Incorrenct')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = 'Log In'
        return context
    

@method_decorator(login_required(login_url="/user/login/"), name='dispatch')
class UserLogoutView(LogoutView) :    
    def get_success_url(self):
        return reverse_lazy('login')


@login_required(login_url="/user/login/")
def profile(req) :
    transections = Transection.objects.filter(user=req.user)
    data = []
    count = {}
    for transection in transections :
        if len(data) == 0 :
            data.append(Car.objects.get(id=transection.car_id))
            count[transection.car_id] = transection.quantity
            print(type(count[transection.car_id]))
        else :
            car = Car.objects.get(id=transection.car_id)
            if transection.car_id in count :
                count[transection.car_id]+=1
            else :
                count[transection.car_id] = transection.quantity
                data.append(car)
    print(type(car.id))
    return render(req, 'user/profile.html', {'data': data, 'count' : count})