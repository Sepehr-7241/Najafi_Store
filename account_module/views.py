from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import RegisterForm, VerifyCodeForm, LoginForm
from .models import OtpCode, User
from utils import send_otp_code
import random


class UserRegisterView(View):
    form_class = RegisterForm
    template_name = 'account_module/register_page.html'

    def get(self, request):
        form = self.form_class
        context = {
            'register_form': form
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(100001, 999999)
            send_otp_code(form.cleaned_data['phone_number'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone_number'],
                'full_name': form.cleaned_data['full_name'],
                'password': form.cleaned_data['password'],
            }
            messages.success(request, 'کد برای شما ارسال شد.')
            return redirect('verify_page')
        return render(request, self.template_name, {'register_form': form})


class UserRegistrationVerifyCodeView(View):
    form_class = VerifyCodeForm

    def get(self, request):
        form = self.form_class
        context = {
            'form': form
        }
        return render(request, 'account_module/verify_page.html', context)

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(
                    user_session['phone_number'],
                    user_session['full_name'],
                    user_session['password'],
                )
                code_instance.delete()
                messages.success(request, 'ثبت نام با موفقیت انجام شد', 'success')
                return redirect('home_page')
            else:
                messages.error(request, 'کد وروردی نامعتبر است', 'danger')
                return redirect('verify_page')
        return redirect('home_page')


class UserLoginView(View):
    form = LoginForm

    def get(self, request):
        form = self.form
        return render(request, 'account_module/login_page.html', {'login_form': form})

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            user = authenticate(request, phone_number=phone_number, password=password)
            if user is not None:
                login(request, user)
                return redirect('home_page')
            else:
                form.add_error(None, 'شماره تلفن یا رمزعبور اشتباه است')
        return render(request, 'account_module/login_page.html', {'login_form': form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('home_page'))
