# Generated by Django 3.1.5 on 2021-02-20 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0033_auto_20210220_1601'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='type',
            field=models.CharField(default='Texual', max_length=200),
        ),
    ]
