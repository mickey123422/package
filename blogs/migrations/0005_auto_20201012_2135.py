# Generated by Django 3.1.2 on 2020-10-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20201012_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.IntegerField(max_length=20),
        ),
    ]
