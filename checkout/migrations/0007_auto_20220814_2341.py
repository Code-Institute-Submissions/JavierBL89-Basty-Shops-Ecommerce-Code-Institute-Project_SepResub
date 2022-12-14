# Generated by Django 3.2 on 2022-08-14 23:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_rename_default_postcode_userprofile_default_post_code'),
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='street_address_1',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='order',
            name='street_address_2',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='profiles.userprofile'),
        ),
    ]
