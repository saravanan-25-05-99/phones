# Generated by Django 4.2.2 on 2023-07-01 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=120)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='images')),
                ('quantity', models.SmallIntegerField()),
                ('seller_detail', models.CharField(max_length=50)),
                ('warranty', models.CharField(max_length=50)),
                ('specification', models.TextField()),
                ('memory', models.CharField(choices=[('1', '2 GB'), ('2', '3 GB'), ('3', '4 GB')], default='1', max_length=4)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
