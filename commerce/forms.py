from django import forms
from django.contrib import admin
from models import Product
from models import Structure
from models import Detail
from models import Property
from models import Category
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
