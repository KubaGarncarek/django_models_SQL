# Generated by Django 4.0.5 on 2022-07-04 14:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_alter_comments_listing_alter_comments_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]