# Generated by Django 5.0.2 on 2024-05-15 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0010_alter_order_product_names"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("PAID", "PAID"),
                    ("DELIVERED", "DELIVERED"),
                    ("FULFILED", "FULFILED"),
                    ("INFULFILED", "INFULFILED"),
                    ("RETURNED", "RETURNED"),
                ],
                max_length=10,
            ),
        ),
    ]
