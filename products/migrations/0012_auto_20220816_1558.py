# Generated by Django 3.2 on 2022-08-16 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_sizes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AddField(
            model_name='productdetail',
            name='set_product_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
