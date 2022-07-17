from django.contrib import admin
from .models import Category, Subcategory, Product, ProductDetail, Review, Size, Image
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
        'pk'
    )


class SubcategoryAdmin(admin.ModelAdmin):

    list_display = (
        'friendly_name',
        'name',
        'pk'
    )


class ProductAdmin(admin.ModelAdmin):

    list_display = (
        'sku',
        'name',
        'category',
        'subcategory_id',
    )
    ordering = ('sku',)


class ProductDetailsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
    )


class ReviewsAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'rating',
    )


class ImagesAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
    )


class SizesAdmin(admin.ModelAdmin):

    list_display = (
        'product_id',
        'size',
        'stock',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductDetail, ProductDetailsAdmin)
admin.site.register(Review, ReviewsAdmin)
admin.site.register(Size, SizesAdmin)
admin.site.register(Image, ImagesAdmin)

