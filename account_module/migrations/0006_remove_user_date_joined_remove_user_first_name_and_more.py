# Generated by Django 5.1.3 on 2024-11-27 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0005_alter_otpcode_code_alter_otpcode_created_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
