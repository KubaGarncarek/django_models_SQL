# Generated by Django 4.0.5 on 2022-06-27 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listings'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(blank=True, related_name='interested_users', to='auctions.listings'),
        ),
    ]
