# Generated by Django 4.2.3 on 2023-07-09 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('headphones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=120)),
                ('lastname', models.CharField(max_length=120)),
                ('course', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
