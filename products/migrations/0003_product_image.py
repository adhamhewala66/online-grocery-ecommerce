# Generated by Django 3.2 on 2022-09-15 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='products/'),
            preserve_default=False,
        ),
    ]
