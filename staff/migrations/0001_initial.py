# Generated by Django 4.1.5 on 2023-01-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_number', models.PositiveIntegerField()),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('day_of_employment', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
