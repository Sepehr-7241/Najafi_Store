from django.shortcuts import render


def about_us_page(request):
    return render(request, 'about_us_module/about_us_page.html')
