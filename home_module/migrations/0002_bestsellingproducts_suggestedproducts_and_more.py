# Generated by Django 5.1.3 on 2024-11-30 14:56

import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_module', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSellingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('image', models.ImageField(upload_to='images/best-selling-products', verbose_name='تصویر')),
                ('url', models.URLField(verbose_name='آدرس اینترنتی محصول')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('is_delete', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
            ],
            options={
                'verbose_name': 'پرفروش ترین محصول',
                'verbose_name_plural': 'پرفروش ترین محصولات',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='SuggestedProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='عنوان')),
                ('description', django_ckeditor_5.fields.CKEditor5Field(verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='images/suggested-products', verbose_name='تصویر')),
                ('url', models.URLField(verbose_name='آدرس اینترنتی محصول')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')),
                ('is_delete', models.BooleanField(default=False, verbose_name='آیا حذف شده است؟')),
            ],
            options={
                'verbose_name': 'محصول پیشنهادی',
                'verbose_name_plural': 'محصولات پیشنهادی',
                'ordering': ['created'],
            },
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'ordering': ['created'], 'verbose_name': 'اسلایدر', 'verbose_name_plural': 'اسلایدرها'},
        ),
        migrations.AlterField(
            model_name='slider',
            name='description',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='توضیحات اسلایدر'),
        ),
        migrations.AlterField(
            model_name='slider',
            name='is_delete',
            field=models.BooleanField(verbose_name='آیا اسلایدر حذف شده؟'),
        ),
    ]
