# Generated by Django 4.1 on 2022-09-12 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_remove_product_images_list_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_reviews',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sizes',
        ),
    ]
