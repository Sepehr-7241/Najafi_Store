# Generated by Django 5.1.3 on 2024-12-01 08:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='زمان انجام لایک')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_module.product', verbose_name='محصول')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'محصول موردپسند',
                'verbose_name_plural': 'محصولات موردپسند',
                'ordering': ['created_at'],
            },
        ),
    ]
