from django import forms


class CartAddProductForm(forms.Form):
    product_quantity_choices = [(i, str(i)) for i in range(1, 21)]

    quantity = forms.TypedChoiceField(
        choices=product_quantity_choices,
        coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
