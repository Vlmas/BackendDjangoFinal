# Generated by Django 4.0.4 on 2022-05-24 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateField()),
                ('num_pages', models.IntegerField(default=1)),
                ('genre', models.CharField(default='', max_length=64)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=128)),
                ('price', models.FloatField(default=0)),
                ('description', models.TextField(default='')),
                ('created_at', models.DateField()),
                ('type', models.CharField(default='Travel', max_length=64)),
            ],
            options={
                'verbose_name': 'Journal',
                'verbose_name_plural': 'Journals',
            },
        ),
    ]
