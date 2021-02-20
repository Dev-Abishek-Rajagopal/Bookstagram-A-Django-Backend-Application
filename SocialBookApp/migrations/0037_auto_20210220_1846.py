# Generated by Django 3.1.5 on 2021-02-20 13:16

from django.db import migrations, models
import django.db.models.deletion
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0036_auto_20210220_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookWishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publist', unixtimestampfield.fields.UnixTimeStampField(auto_now=True, null=True)),
                ('Book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SocialBookApp.app_user')),
            ],
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]