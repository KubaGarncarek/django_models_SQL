# Generated by Django 4.0.5 on 2022-06-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_closed_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='listings',
            name='highest_bidder',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Closed_Listings',
        ),
    ]
