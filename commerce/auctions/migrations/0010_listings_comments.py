# Generated by Django 4.0.5 on 2022-07-04 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_listings_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='comments',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]
