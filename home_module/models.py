from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class Slider(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان اسلایدر')
    description = CKEditor5Field(verbose_name='توضیحات اسلایدر')
    image = models.ImageField(upload_to='images/slider', verbose_name='تصویراسلایدر')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_delete = models.BooleanField(verbose_name='آیا اسلایدر حذف شده؟')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = 'اسلایدر'
        verbose_name_plural = 'اسلایدرها'


class BestSellingProducts(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    image = models.ImageField(upload_to='images/best-selling-products', verbose_name='تصویر')
    url = models.URLField(verbose_name='آدرس اینترنتی محصول')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_delete = models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = 'پرفروش ترین محصول'
        verbose_name_plural = 'پرفروش ترین محصولات'


class SuggestedProducts(models.Model):
    title = models.CharField(max_length=50, verbose_name='عنوان')
    description = CKEditor5Field(verbose_name='توضیحات')
    image = models.ImageField(upload_to='images/suggested-products', verbose_name='تصویر')
    url = models.URLField(verbose_name='آدرس اینترنتی محصول')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    is_delete = models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created']
        verbose_name = 'محصول پیشنهادی'
        verbose_name_plural = 'محصولات پیشنهادی'
