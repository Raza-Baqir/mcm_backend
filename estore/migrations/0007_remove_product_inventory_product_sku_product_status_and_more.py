# Generated by Django 4.2.12 on 2025-05-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estore", "0006_remove_product_product_gallery_productgallery"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="inventory",
        ),
        migrations.AddField(
            model_name="product",
            name="SKU",
            field=models.CharField(default="sku", max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name="product",
            name="status",
            field=models.CharField(default="active", max_length=100),
        ),
        migrations.AddField(
            model_name="product",
            name="stock",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name="Inventory",
        ),
    ]
