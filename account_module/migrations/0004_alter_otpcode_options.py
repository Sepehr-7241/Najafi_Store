# Generated by Django 5.1.3 on 2024-11-26 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0003_otpcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otpcode',
            options={'verbose_name': 'کد یکبارمصرف', 'verbose_name_plural': 'کدهای یکبارمصرف'},
        ),
    ]