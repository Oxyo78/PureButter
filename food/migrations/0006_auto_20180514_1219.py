# Generated by Django 2.0.4 on 2018-05-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20180513_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.CharField(max_length=150),
        ),
    ]
