from . forms import SignUpForm, User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy


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
    

@method_decorator(login_required(login_url="/author/login/"), name='dispatch')
class UserLogoutView(LogoutView) :    
    def get_success_url(self):
        return reverse_lazy('login')