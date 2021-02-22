# Generated by Django 3.1.5 on 2021-02-22 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0038_book_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app_user',
            name='email',
            field=models.CharField(default='', max_length=200, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='app_user',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
