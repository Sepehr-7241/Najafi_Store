from django.contrib import admin
from .models import Slider, BestSellingProducts, SuggestedProducts


class HomePageAdmin(admin.ModelAdmin):
    list_display = ['title', 'created', 'is_delete']
    list_editable = ['is_delete']


admin.site.register(Slider, HomePageAdmin)
admin.site.register(BestSellingProducts, HomePageAdmin)
admin.site.register(SuggestedProducts, HomePageAdmin)
