# Generated by Django 3.1.5 on 2021-02-16 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0025_auto_20210217_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendlist',
            name='relationship',
            field=models.CharField(max_length=200),
        ),
    ]
