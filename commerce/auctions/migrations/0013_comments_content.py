# Generated by Django 4.0.5 on 2022-07-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_coments_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='content',
            field=models.CharField(default=1, max_length=128),
            preserve_default=False,
        ),
    ]
