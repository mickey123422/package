# Generated by Django 3.1.2 on 2020-12-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_auto_20201201_2324'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='email',
            field=models.TextField(max_length=200, null=True),
        ),
    ]
