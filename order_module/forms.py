from django import forms


class CartAddForm(forms.Form):
    quantity = forms.IntegerField(
        min_value=1,
        max_value=20,
        label='مقدار(کیلوگرم)',
        widget=forms.NumberInput(attrs={
            'class': 'btn btn-success',
            'id': 'var-value',
            'value': '1'
        }))


class CouponApplyForm(forms.Form):
    code = forms.CharField(
        label='کد تخفیف ',
        required=False,

    )
