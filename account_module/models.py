from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=225, unique=True, blank=True, null=True, verbose_name='ایمیل')
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه')
    full_name = models.CharField(max_length=225, verbose_name='نام و نام خانوادگی')
    is_active = models.BooleanField(default=True, verbose_name='آیا کاربر فعال است؟')
    is_admin = models.BooleanField(default=False, verbose_name='آیا کاربر ادمین است؟')

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    @property
    def is_staff(self):
        return self.is_admin


class OtpCode(models.Model):
    phone_number = models.CharField(max_length=11, unique=True, verbose_name='تلفن همراه')
    code = models.PositiveSmallIntegerField(verbose_name='کد')
    created = models.DateTimeField(auto_now=True, verbose_name='تاریخ ارسال')

    class Meta:
        verbose_name = 'کد یکبارمصرف'
        verbose_name_plural = 'کدهای یکبارمصرف'

    def __str__(self):
        return f'{self.phone_number} - {self.code}'
