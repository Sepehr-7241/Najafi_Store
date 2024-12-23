from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
from product_module.models import Product
import uuid


class Order(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    paid = models.BooleanField(default=False, verbose_name='آیا پرداخت شده؟')
    created = models.DateTimeField(auto_now_add=True, verbose_name='ساخته شده در زمان:')
    updated = models.DateTimeField(auto_now=True, verbose_name='به روزرسانی شده در زمان:')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name='آیدی')
    discount = models.IntegerField(blank=True, null=True, default=None, verbose_name='تخفیف')

    class Meta:
        ordering = ('paid', '-updated')
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'

    def get_total_price(self):
        total = sum(item.get_cost() for item in self.items.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', verbose_name='سبد خرید')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول')
    price = models.IntegerField(verbose_name='قیمت')
    quantity = models.IntegerField(default=1, verbose_name='تعداد')

    def get_cost(self):
        return self.price * self.quantity


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True, verbose_name='کد')
    valid_from = models.DateTimeField(verbose_name='تاریخ ثبت')
    valid_to = models.DateTimeField(verbose_name='تاریخ انقضا')
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(90)], verbose_name='مقدار تخفیف')
    active = models.BooleanField(default=False, verbose_name='آیا فعال است؟')

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کدهای تخفیف'

    def __str__(self):
        return self.code
