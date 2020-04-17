from django.shortcuts import render, redirect, reverse
from django.views import View
from .forms import SignUpForm, SignInForm
from .models import User
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'index.html')


class SingUpView(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
        else:
            print(form.errors.get_json_data())
            return redirect(reverse('signup'))


class SingInView(View):
    def get(self, request):
        return render(request, 'signin.html')

    def post(self, request):
        form = SignInForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password')).first()
            if user:
                request.session['user_id'] = user.id
                return redirect(reverse('index'))
            else:
                messages.info(request, '用户名或密码错误')
                return redirect(reverse('signin'))
        else:
            print(form.get_errors())
            messages.info(request, form.get_errors())
            return redirect(reverse('signin'))