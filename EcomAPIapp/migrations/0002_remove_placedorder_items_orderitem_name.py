# Generated by Django 4.0.3 on 2022-10-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EcomAPIapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='placedorder',
            name='items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
