# Generated by Django 3.1 on 2021-04-28 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20210428_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://img.buzzfeed.com/thumbnailer-prod-us-east-1/video-api/assets/216054.jpg', max_length=500),
        ),
    ]
