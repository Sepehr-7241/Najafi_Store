from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.conf import settings
from .cart import Cart
from .forms import CartAddForm, CouponApplyForm
from .models import Order, OrderItem, Coupon
from product_module.models import Product
import requests
import json
import datetime


class CartView(View):
    def get(self, request):
        cart = Cart(request)
        return render(request, 'order_module/basket_page.html', {'cart': cart})


class CartAddView(View):
    def post(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddForm(request.POST)
        if form.is_valid():
            cart.add(product, form.cleaned_data['quantity'])

        return redirect('cart_page')


class CartRemoveView(View):
    def get(self, request, product_id):
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart_page')


class OrderDetailView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        form = CouponApplyForm
        order = get_object_or_404(Order, id=order_id)
        return render(request, 'order_module/order_page.html', {'order': order, 'form': form})


class OrderCreateView(LoginRequiredMixin, View):
    def get(self, request):
        cart = Cart(request)
        order = Order.objects.create(user=request.user)
        for item in cart:
            OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('order_detail', order.id)


if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'

ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"
CallbackURL = 'http://127.0.0.1:8000/cart/verify/'


class OrderPayView(LoginRequiredMixin, View):
    def get(self, request, order_id):
        order = get_object_or_404(Order, id=order_id, user=request.user)
        request.session['order_pay'] = {
            'order_id': str(order.id)
        }
        data = {
            "MerchantID": settings.MERCHANT,
            "Amount": float(order.get_total_price() * 10),
            "Description": description,
            "Phone": request.user.phone_number,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        headers = {'accept': 'application/json', 'content-type': 'application/json', 'content-length': str(len(data))}
        try:
            response = requests.post(ZP_API_REQUEST, data=data, headers=headers, timeout=10)

            if response.status_code == 200:
                response_json = response.json()
                authority = response_json['Authority']
                if response_json['Status'] == 100:
                    return redirect(ZP_API_STARTPAY + authority)
                else:
                    return HttpResponse('Error')
            return HttpResponse('response failed')
        except requests.exceptions.Timeout:
            return HttpResponse('Timeout Error')
        except requests.exceptions.ConnectionError:
            return HttpResponse('Connection Error')


class OrderVerifyView(LoginRequiredMixin, View):
    def get(self, request):
        order_id = request.session['order_pay']['order_id']
        order = Order.objects.get(id=order_id)
        authority = request.GET.get('Authority')
        status = request.GET.get('Status')
        if status == 'OK' and authority:
            data = {
                "MerchantID": settings.MERCHANT,
                "Amount": float(order.get_total_price() * 10),
                "Authority": authority,
            }
            data = json.dumps(data)
            headers = {'accept': 'application/json', 'content-type': 'application/json',
                       'content-length': str(len(data))}
            try:
                response = requests.post(ZP_API_VERIFY, data=data, headers=headers)
                if response.status_code == 200:
                    response_json = response.json()
                    reference_id = response_json['RefID']
                    if response['Status'] == 100:
                        return HttpResponse(f'successful , RefID: {reference_id}')
                    else:
                        return HttpResponse('Error')
                return HttpResponse('response failed')
            except requests.exceptions.Timeout:
                return HttpResponse('Timeout Error')
            except requests.exceptions.ConnectionError:
                return HttpResponse('Connection Error')
        else:
            return HttpResponse('Not ok')


class CouponApplyView(LoginRequiredMixin, View):
    def post(self, request, order_id):
        now = datetime.datetime.now()
        form = CouponApplyForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            try:
                coupon = Coupon.objects.get(code__exact=code, valid_from__lte=now, valid_to__gte=now, active=True)
            except Coupon.DoesNotExist:
                return redirect('order_detail', order_id)
            order = Order.objects.get(id=order_id)
            order.discount = coupon.discount
            order.save()
            return redirect('order_detail', order_id)
