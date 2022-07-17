from django.contrib import admin
from .models import Category, Subcategory, Product, ProductDetail, Review, Size, Image

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
        'pk'
    )
    list_filter = ('name', )
    search_fields = ['name']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
        'pk'
    )
    list_filter = ('name',)
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'subcategory_id',
        'pk',
    )
    ordering = ('sku',)
    list_filter = ('name', 'category', 'subcategory_id')
    search_fields = ['name', 'sku', 'category', 'subcategory_id']


@admin.register(ProductDetail)
class ProductDetailsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
    )
    list_filter = ('product_id',)
    search_fields = ['product_id']


@admin.register(Review)
class ReviewsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'rating',
    )
    list_filter = ('product_id',)
    search_fields = ['product_id']


@admin.register(Image)
class ImagesAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
    )
    list_filter = ('product_id',)
    search_fields = ['product_id']


@admin.register(Size)
class SizesAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'size',
        'stock',
    )
    list_filter = ('product_id', 'size')
    search_fields = ['product_id', 'size']

