# Generated by Django 4.1.5 on 2023-01-07 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('address', models.CharField(max_length=100)),
                ('grade', models.PositiveIntegerField()),
                ('major', models.CharField(max_length=100)),
            ],
        ),
    ]
