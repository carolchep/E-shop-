# Generated by Django 2.2 on 2021-12-11 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('S', 'Cleanser'), ('SW', 'Toner'), ('OW', 'Moisturizer')], max_length=2),
        ),
    ]
