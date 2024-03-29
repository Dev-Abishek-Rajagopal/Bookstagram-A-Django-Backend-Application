# Generated by Django 3.1.5 on 2021-03-24 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialBookApp', '0024_txtpostcommentsnewsfeed'),
    ]

    operations = [
        migrations.AddField(
            model_name='txtpostcomments',
            name='dp',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='txtpostcomments',
            name='header',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='txtpostcomments',
            name='related',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='txtpostcomments',
            name='share',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='txtpostcomments',
            name='types',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='txtpostcomments',
            name='url',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='txtpostcomments',
            name='comments',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='txtpostcomments',
            name='post',
            field=models.TextField(),
        ),
    ]
