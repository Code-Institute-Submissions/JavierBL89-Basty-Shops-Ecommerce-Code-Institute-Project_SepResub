from django.contrib import admin
from .models import Category, Subcategory, Product, ProductDetail, Review, Size, Image
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
        'pk'
    )
    list_filter = ('name', )
    search_fields = ['name']


class SubcategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
        'pk'
    )
    list_filter = ('name',)
    search_fields = ['name']


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


class ProductDetailsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
    )
    list_filter = ('product_id',)
    search_fields = ['product_id']
    


class ReviewsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'rating',
    )
    list_filter = ('product_id',)
    search_fields = ['product_id']


class ImagesAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
    )
    list_filter = ('product_id',)
    search_fields = ['product_id']


class SizesAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'size',
        'stock',
    )
    list_filter = ('product_id', 'size')
    search_fields = ['product_id', 'size']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailsAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Size, SizesAdmin)
admin.site.register(Image, ImagesAdmin)

