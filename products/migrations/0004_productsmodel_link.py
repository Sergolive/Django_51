# Generated by Django 5.0.6 on 2024-05-28 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_productsmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsmodel',
            name='link',
            field=models.TextField(null=True),
        ),
    ]
