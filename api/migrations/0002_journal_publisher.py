# Generated by Django 4.0.4 on 2022-05-24 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='publisher',
            field=models.CharField(default='Almas', max_length=64),
        ),
    ]