# Generated by Django 4.1.7 on 2023-04-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rev', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regulations_with_Grades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Regulation', models.CharField(max_length=20)),
                ('Lower_limit', models.IntegerField()),
                ('Upper_limit', models.IntegerField()),
                ('Grades', models.CharField(max_length=2)),
            ],
        ),
    ]
