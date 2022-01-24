# Generated by Django 4.0.1 on 2022-01-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_product_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Accessories', (('Bags', 'Bags'), ('Gloves', 'Gloves'), ('Hair', 'Hair'), ('Hats', 'Hats'), ('Jewellery', 'Jewellery'), ('Socks', 'Socks'), ('Sunglasses', 'Sunglasses'), ('Tights', 'Tights'))), ('Clothing', (('Coats + Jackets', 'Coats + Jackets'), ('Dresses', 'Dresses'), ('Jeans', 'Jeans'), ('Knitwear', 'Knitwear'), ('Shorts', 'Shorts'), ('Skirts', 'Skirts'), ('Sweatshirt', 'Sweatshirt'), ('T-shirts', 'T-shirts'), ('Trackpants', 'Trackpants'), ('Trousers', 'Trousers'))), ('Shoes', (('Boots', 'Boots'), ('Flats', 'Flats'), ('Heels', 'Heels'), ('Trainers', 'Trainers'))), ('Skincare', (('Skincare', 'Skincare'), ('Makeup', 'Makeup'), ('Home', 'Home')))], max_length=50),
        ),
    ]
