# Generated by Django 3.1.7 on 2021-04-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20210405_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='post_title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='post_id',
            field=models.CharField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
