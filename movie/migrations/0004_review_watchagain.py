# Generated by Django 4.1.1 on 2022-09-16 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='watchAgain',
            field=models.BooleanField(default=False),
        ),
    ]
