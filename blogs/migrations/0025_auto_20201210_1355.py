# Generated by Django 3.1.2 on 2020-12-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0024_auto_20201207_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='size',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
