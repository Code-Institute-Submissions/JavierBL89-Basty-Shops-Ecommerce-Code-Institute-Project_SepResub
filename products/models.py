from django.db import models

# Create your models here.


class Category(models.Model):
    """ Class for subcategories """
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    def __string__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Subcategory(models.Model):
    """ Class for subcategories """
    class Meta:
        verbose_name_plural = 'Subcategories'

    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, blank=True, null=True)

    def __string__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    Class for products
    """
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL,
                                 related_name='category')
    subcategory_id = models.ForeignKey('Subcategory',
                                       null=True,
                                       blank=True,
                                       on_delete=models.SET_NULL,
                                       related_name='subcategory_id')
    name = models.CharField(max_length=254)
    title = models.CharField(max_length=254, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(null=True)
    product_details = models.ForeignKey('ProductDetail',
                                        null=True,
                                        blank=True,
                                        on_delete=models.SET_NULL)
    sizes = models.BooleanField(default=True, blank=True)
    product_reviews = models.ForeignKey('Review',
                                        null=True,
                                        blank=True,
                                        on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    cover_image = models.ImageField(null=True, blank=True)

    def __string__(self):
        return self.name


class ProductDetail(models.Model):
    """
    Class for product details
    """
    product_id = models.ForeignKey('Product',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
    heels_mesurement = models.CharField(max_length=254, null=True, blank=True)
    upper_material = models.CharField(max_length=254, null=True, blank=True)
    sole = models.CharField(max_length=254, null=True, blank=True)
    technology = models.CharField(max_length=254, null=True, blank=True)
    lining_material = models.CharField(max_length=254, null=True, blank=True)
    fastening = models.CharField(max_length=254, null=True, blank=True)

    def __string__(self):
        return self.product_id


class Size(models.Model):
    """
    Class for product sizes
    """
    product_id = models.ForeignKey('Product',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
    size = models.CharField(max_length=2, null=True)
    stock = models.PositiveSmallIntegerField(null=True)

    def __string__(self):
        return f'{self.size}  {self.stock}'


class Review(models.Model):
    """
    Class for product reviews
    """
    product_id = models.ForeignKey('Product',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
    quote = models.TextField(null=True, blank=True)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True)
    date = models.DateField(auto_now=True)

    def __string__(self):
        return f'{self.product_id} {self.rating} {self.date}'


class Image(models.Model):

    product_id = models.ForeignKey('Product',
                                   null=True,
                                   blank=True,
                                   on_delete=models.CASCADE)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)
    image4 = models.ImageField(null=True, blank=True)

    def __string__(self):
        return f'{self.product_id} {self.image1}\
                 {self.image2} {self.image3} {self.image4}'
