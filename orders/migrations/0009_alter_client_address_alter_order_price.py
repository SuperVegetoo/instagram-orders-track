# Generated by Django 5.0.2 on 2024-05-07 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0008_remove_order_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="address",
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name="order",
            name="price",
            field=models.CharField(max_length=10),
        ),
    ]