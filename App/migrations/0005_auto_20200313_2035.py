# Generated by Django 2.0 on 2020-03-13 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_publication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='booktitle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
