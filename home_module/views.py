from django.shortcuts import render
from django.views import View
from .models import Slider, SuggestedProducts, BestSellingProducts
from product_module.models import FooterProductCategory


class HomeView(View):
    def get(self, request):
        sliders = Slider.objects.filter(is_delete=False)[:3]
        suggested_products = SuggestedProducts.objects.filter(is_delete=False)[:3]
        best_selling_products = BestSellingProducts.objects.filter(is_delete=False)[:3]
        context = {
            'sliders': sliders,
            'best_selling_products': best_selling_products,
            'suggested_products': suggested_products,
        }
        return render(request, 'home_module/index.html', context)


def site_header_partial(request):
    return render(request, 'shared/site_header_partial.html')


def site_footer_partial(request):
    footer = FooterProductCategory.objects.filter(is_active=True)[:5]
    return render(request, 'shared/site_footer_partial.html', {'footer': footer})
