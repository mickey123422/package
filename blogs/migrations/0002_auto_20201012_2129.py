# Generated by Django 3.1.2 on 2020-10-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.IntegerField(),
        ),
    ]