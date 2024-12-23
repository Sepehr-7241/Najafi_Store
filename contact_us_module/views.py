from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactUsForm


class ContactUsView(View):
    def get(self, request):
        form = ContactUsForm()
        return render(request, 'contact_us_module/contact_us_page.html', context={
            'form': form
        })

    def post(self, request):
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')

        return render(request, 'contact_us_module/contact_us_page.html', context={
            'form': form
        })
