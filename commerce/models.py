from django.db import models
from topnotchdev import files_widget
from django.utils.translation import ugettext_lazy as _


class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    TYPES = (
        ('number', 'Number'),
        ('boolean', 'Boolean'),
        ('text', 'Text'),
    )
    type = models.CharField(choices=TYPES, max_length=15, verbose_name=_('Field Type'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Property')
        verbose_name_plural = _('Product Properties')


class Structure(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    properties = models.ManyToManyField(Property, verbose_name=_('Properties'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Structure')
        verbose_name_plural = _('Product Structures')


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    image = models.FileField(null=True, verbose_name=_('Image'), upload_to='static/media/')
    structures = models.ManyToManyField(Structure, verbose_name=_('Product Structures'))
    parent = models.ForeignKey("self", blank=True, null=True, verbose_name=_('Parent Category'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    long_name = models.CharField(max_length=255, verbose_name=_('Long Name'), blank=True)
    description = models.TextField(null=True, verbose_name=_('Description'))
    category = models.ForeignKey(Category, verbose_name=_('Category'), null=True)
    price = models.FloatField(default=0, verbose_name=_('Price'))
    image = models.ImageField(null=True, upload_to='static/media', verbose_name=_('Product Main Image'))
    images = files_widget.ImagesField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('Date'))

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class Prices(models.Model):
    date = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('Date'))
    amount = models.FloatField()
    product = models.ForeignKey(Product)

    class Meta:
        verbose_name = _('Price')
        verbose_name_plural = _('Prices')


class Detail(models.Model):
    property = models.ForeignKey(Property, verbose_name=_('Product Property'))
    value = models.CharField(max_length=255, verbose_name=_('Value'))
    product = models.ForeignKey(Product, verbose_name=_('Product'))

    class Meta:
        verbose_name = _('Product Detail')
        verbose_name_plural = _('Product Details')