# Generated by Django 4.2.1 on 2023-05-21 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mylist', '0006_rename_reporter_shoppingitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingitem',
            name='user',
            field=models.ForeignKey(db_column='user', default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
