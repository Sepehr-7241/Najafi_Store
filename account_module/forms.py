from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core import validators
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField
from .models import User
import re

messages = {
    'required': 'لطفا تمام فیلدها را پر کنید',
    'max_length': 'تعداد کاراکترهای ورودی بیشتر از حد مجاز است',
    'mix_length': 'تعداد کاراکترهای ورودی کمتر از حد مجاز است',
}


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['phone_number', 'full_name']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] and cd['confirm_password'] and cd['password'] != cd['confirm_password']:
            raise ValidationError('رمزعبور و تایید رمزعبور با یکدیگر تطابق ندارند')
        return cd['confirm_password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['confirm_password'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        help_text="you can change password using <a href=\"../password/\"> this form </a>")

    class Meta:
        model = User
        fields = ['email', 'phone_number', 'full_name', 'password', 'last_login']


class RegisterForm(forms.Form):
    phone_number = forms.CharField(
        error_messages=messages,
        widget=forms.TextInput(attrs={
            'id': 'style3',
            'placeholder': 'تلفن همراه'
        }),
        validators=[
            validators.MaxLengthValidator(11),
            validators.MinLengthValidator(10)
        ]
    )
    full_name = forms.CharField(
        error_messages=messages,
        widget=forms.TextInput(attrs={
            'id': 'style3',
            'placeholder': 'نام و نام خانوادگی'
        }),
        validators=[
            validators.MaxLengthValidator(50),

        ]
    )
    password = forms.CharField(
        error_messages=messages,
        widget=forms.PasswordInput(attrs={
            'id': 'style3',
            'placeholder': 'رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(20),
        ]
    )
    confirm_password = forms.CharField(
        error_messages=messages,
        widget=forms.PasswordInput(attrs={
            'id': 'style3',
            'placeholder': 'تکرار رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(20),
        ]
    )
    captcha = CaptchaField(error_messages=messages)

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise ValidationError('رمز عبور باید حداقل 8 کاراکتر باشد')
        if not re.search(r"[A-Z]", password):
            raise ValidationError('رمزعبور باید حداقل یک حرف بزرگ داشته باشد')
        if not re.search(r"[0-9]", password):
            raise ValidationError('رمزعبور باید حداقل یک عدد داشته باشد')
        return password

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password == confirm_password:
            return password
        else:
            raise ValidationError('کلمه ی عبور با تکرار کلمه ی عبور مغایرت دارد')


class LoginForm(forms.Form):
    phone_number = forms.CharField(
        error_messages=messages,
        widget=forms.TextInput(attrs={
            'id': 'style3',
            'placeholder': 'تلفن همراه'
        }),
        validators=[
            validators.MaxLengthValidator(11),
            validators.MinLengthValidator(10)
        ]
    )
    password = forms.CharField(
        error_messages=messages,
        widget=forms.PasswordInput(attrs={
            'id': 'style3',
            'placeholder': 'رمزعبور'
        }),
        validators=[
            validators.MaxLengthValidator(20),
        ]
    )
    captcha = CaptchaField(error_messages=messages)


class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(
        error_messages=messages,
        widget=forms.TextInput(attrs={
            'id': 'style3',
            'placeholder': 'کد'
        })
    )
