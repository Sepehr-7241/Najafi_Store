from django import forms


class ProductFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        label='',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': "form-control",
            'id': 'inputModalSearch',
            'placeholder': ' ... جستجو',

        })
    )
