# Generated by Django 5.1.6 on 2025-03-03 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_alter_product_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
