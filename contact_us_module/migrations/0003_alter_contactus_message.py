# Generated by Django 5.1.3 on 2024-11-30 15:51

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact_us_module', '0002_remove_contactus_is_read_by_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name='متن تماس با ما'),
        ),
    ]
