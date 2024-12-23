from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field


class Category(models.Model):
    title = models.CharField(max_length=225, verbose_name='عنوان')
    url_title = models.SlugField(max_length=225, unique=True, verbose_name='نام url محصول')
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name='scategory', null=True, blank=True,
                                     verbose_name='زیرمجموعه')
    is_sub = models.BooleanField(default=False, verbose_name='آیا زیرمجموعه دارد؟')

    class Meta:
        ordering = ['title']
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=300, verbose_name='نام محصول')
    category = models.ManyToManyField(Category, related_name='product_categories', verbose_name='دسته بندی ها')
    image = models.ImageField(upload_to='images/product', null=True, blank=True, verbose_name='تصویر محصول')
    price = models.IntegerField(verbose_name='قیمت')
    description = CKEditor5Field(verbose_name='توضیحات محصول')
    is_active = models.BooleanField(default=True, verbose_name='آیا محصول فعال است؟')
    is_delete = models.BooleanField(verbose_name='آیا محصول حذف شده است؟')
    slug = models.SlugField(default='', null=False, blank=True, max_length=200, unique=True, allow_unicode=True,
                            verbose_name='url محصول')

    class Meta:
        ordering = ['title']
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product_detail_page', args=[self.slug])


class LikeProduct(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان انجام لایک')

    def __str__(self):
        return f'{self.user} - {self.product} - {self.created_at}'

    class Meta:
        verbose_name = 'محصول موردپسند'
        verbose_name_plural = 'محصولات موردپسند'
        ordering = ['created_at']


class FooterProductCategory(models.Model):
    title = models.CharField(max_length=225, verbose_name='عنوان فوتر')
    url = models.URLField(verbose_name='url فوتر')
    is_active = models.BooleanField(default=True, verbose_name='آیا فعال است؟')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصولات در فوتر'
        verbose_name_plural = 'دسته بندی های محصولات در فوتر'
