# Generated by Django 4.2.2 on 2023-07-12 17:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("viewer", "0005_rented_returned_reserved"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rented",
            name="rent_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
