# Generated by Django 4.0.5 on 2022-06-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_listings_highest_bidder_delete_closed_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='photo',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
