# Generated by Django 4.2.3 on 2023-07-19 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0010_rented_canceled'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['id_book', '-created']},
        ),
    ]
