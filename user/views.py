from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from user.forms import RegisterUserForm


# Create your views here.



class RegisterUserView(generic.CreateView):
    form_class = RegisterUserForm
    template_name = 'user/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home_view')

class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'

    def get_success_url(self):
        return reverse_lazy('home_view')

def logout_user_view(request):
    logout(request)
    return redirect('login')