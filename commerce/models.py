from django.db import models
from topnotchdev import files_widget
from django.utils.translation import ugettext_lazy as _


class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    type = models.CharField(choices=(
        ('number', 'Number'),
        ('boolean', 'Boolean'),
        ('text', 'Text'),
    ), max_length=15, verbose_name=_('Field Type'))

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
    image = models.FileField(null=True, verbose_name=_('Image'), upload_to='category/')
    structures = models.ManyToManyField(Structure, verbose_name=_('Product Structures'))
    parent = models.ForeignKey("self", blank=True, null=True, verbose_name=_('Parent Category'),
                               related_name='children')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Product Category')
        verbose_name_plural = _('Product Categories')


class Brand(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    logo = models.FileField(null=True, verbose_name=_('Image'), upload_to='category/')
    category = models.ManyToManyField(Category, verbose_name=_('Categories related this brand'), related_name="brands")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brands')


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    long_name = models.CharField(max_length=255, verbose_name=_('Long Name'))
    description = models.TextField(null=True, verbose_name=_('Description'))
    category = models.ForeignKey(Category, verbose_name=_('Category'), null=True)
    brand = models.ForeignKey(Brand, verbose_name=_('Brand'))
    price = models.FloatField(default=0, verbose_name=_('Price'))
    image = models.ImageField(null=True, upload_to='product/', verbose_name=_('Product Main Image'))
    images = files_widget.ImagesField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('Date'))
    available = models.BooleanField(default=True, verbose_name=_('Is Available'))

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
    product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='details')

    class Meta:
        verbose_name = _('Product Detail')
        verbose_name_plural = _('Product Details')


class Slider(models.Model):
    image = models.ImageField(null=True, upload_to='product/', verbose_name=_('Picture'))
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    description = models.CharField(max_length=255, verbose_name=_('Description'))
    show = models.BooleanField(default=True, verbose_name=_('Show'))

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = _('Slider Picture')
        verbose_name_plural = _('Slider Pictures')