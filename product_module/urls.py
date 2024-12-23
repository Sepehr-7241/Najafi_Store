from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_page'),
    re_path(r'detail/(?P<slug>[-\w]+)/', views.ProductDetailView.as_view(), name='product_detail_page'),
    path('category/<slug:category_slug>', views.ProductListView.as_view(), name='category_filter_page'),
    path('like/<int:product_id>', views.LikedProducts.as_view(), name='like_product'),
    path('liked-products/', views.LikedProductsList.as_view(), name='liked_products'),
    path('remove-liked-products/<int:product_id>/', views.RemoveLikedProducts.as_view(), name='remove_liked_products'),
]
