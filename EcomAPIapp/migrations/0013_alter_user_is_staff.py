# Generated by Django 4.0.3 on 2022-11-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAPIapp', '0012_alter_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
