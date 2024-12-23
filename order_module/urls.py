from django.urls import path
from . import views

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_page'),
    path('add/<int:product_id>/', views.CartAddView.as_view(), name='cart_add'),
    path('remove/<int:product_id>/', views.CartRemoveView.as_view(), name='cart_remove'),
    path('detail/<uuid:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('pay/<uuid:order_id>/', views.OrderPayView.as_view(), name='pay_order'),
    path('verify/', views.OrderVerifyView.as_view(), name='verify_order'),
    path('apply/<uuid:order_id>/', views.CouponApplyView.as_view(), name='apply_coupon'),
]
