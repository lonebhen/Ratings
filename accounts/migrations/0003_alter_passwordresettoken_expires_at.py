# Generated by Django 4.2.1 on 2023-09-13 18:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_passwordresettoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passwordresettoken',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 18, 56, 20, 479019, tzinfo=datetime.timezone.utc)),
        ),
    ]
