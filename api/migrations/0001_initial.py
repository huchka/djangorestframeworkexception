# Generated by Django 4.0.3 on 2022-03-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=100)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
                ('modified_datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
