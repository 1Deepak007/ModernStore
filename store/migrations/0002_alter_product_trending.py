# Generated by Django 4.1.6 on 2023-03-16 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default, 1-Trending'),
        ),
    ]
