from django import forms
from models import Product
from models import Detail
from django.forms.models import inlineformset_factory


class ProductForm(forms.ModelForm):
    temp_id = forms.MultiValueField()

    class Meta:
        model = Product


class DetailForm(forms.ModelForm):
    class Meta:
        model = Detail
        exclude = ('product', )


ProductFormSet = inlineformset_factory(Product, Detail, extra=0, min_num=1, fields=('value', 'property',))