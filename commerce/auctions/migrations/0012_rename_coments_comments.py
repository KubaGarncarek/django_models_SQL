# Generated by Django 4.0.5 on 2022-07-04 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_listings_comments_coments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coments',
            new_name='Comments',
        ),
    ]
