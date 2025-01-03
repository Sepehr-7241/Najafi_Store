# Generated by Django 5.1.3 on 2024-12-21 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_remove_product_url_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='آیا محصول فعال است؟'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(allow_unicode=True, blank=True, default='', max_length=200, unique=True, verbose_name='url محصول'),
        ),
    ]
