# Generated by Django 2.2.6 on 2019-11-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0005_auto_20191124_2145"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="unit_price",
            field=models.DecimalField(
                blank=True, decimal_places=4, max_digits=10, null=True
            ),
        ),
    ]
