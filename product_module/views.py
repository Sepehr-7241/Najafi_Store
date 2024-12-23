from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category, LikeProduct
from .forms import ProductFilterForm
from order_module.forms import CartAddForm


class ProductListView(View):
    def get(self, request, category_slug=None):
        # Base QuerySet for active and non-deleted products
        product_queryset = Product.objects.filter(is_active=True, is_delete=False)

        # Filter by category
        if category_slug:
            try:
                category = Category.objects.get(url_title=category_slug)
                product_queryset = product_queryset.filter(category=category)
            except Category.DoesNotExist:
                category = None

        # Searching
        filter_form = ProductFilterForm(request.GET)
        if filter_form.is_valid() and 'search' in request.GET:
            search_query = filter_form.cleaned_data['search']
            product_queryset = product_queryset.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

        # Sorting
        sort_option = request.GET.get('sort', 'asc')
        if sort_option == 'desc':
            product_queryset = product_queryset.order_by('-price')
        else:
            product_queryset = product_queryset.order_by('price')

        # Pagination
        paginator = Paginator(product_queryset, 9)
        page_number = request.GET.get("page")
        products = paginator.get_page(page_number)

        # Context for the template
        context = {
            'products': products,
            'product_filter': filter_form,
        }
        return render(request, 'product_module/product_page.html', context)


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        order_form = CartAddForm
        context = {
            'product': product,
            'order_form': order_form,
        }
        return render(request, 'product_module/product_detail.html', context)


class LikedProducts(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        like = LikeProduct.objects.filter(product=product, user=request.user)
        if like.exists():
            messages.error(request, 'شما قبلا این محصول را لایک کرده اید')
        else:
            LikeProduct.objects.create(product=product, user=request.user)
            messages.success(request, 'محصول با موفقیت لایک شد')
        return redirect('product_page')


class LikedProductsList(LoginRequiredMixin, View):
    def get(self, request):
        liked_products = LikeProduct.objects.filter(user=request.user).select_related('product')
        return render(request, 'product_module/liked_products.html', {'liked_products': liked_products})


class RemoveLikedProducts(LoginRequiredMixin, View):
    def get(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        try:
            like = LikeProduct.objects.get(user=request.user, product=product)
            like.delete()
        except LikeProduct.DoesNotExist:
            pass  # If the like doesn't exist, do nothing

        return redirect('liked_products')


def product_category_component(request):
    categories = Category.objects.filter(is_sub=False)
    context = {
        'categories': categories
    }
    return render(request, 'includes/product_category_component.html', context)
