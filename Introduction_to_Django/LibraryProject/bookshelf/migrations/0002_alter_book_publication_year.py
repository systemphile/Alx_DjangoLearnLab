# Generated by Django 5.0.6 on 2025-07-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshelf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publication_year',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
