# Generated by Django 3.1.5 on 2021-02-20 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0032_auto_20210220_0412'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profilecomment',
            old_name='friend',
            new_name='chatter',
        ),
    ]