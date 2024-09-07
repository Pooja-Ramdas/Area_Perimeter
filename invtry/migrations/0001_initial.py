# Generated by Django 5.1.1 on 2024-09-07 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drugid', models.IntegerField(max_length=64)),
                ('name', models.CharField(max_length=256)),
                ('manufacturer', models.CharField(max_length=512)),
                ('drugtype', models.CharField(max_length=128)),
                ('quantity', models.IntegerField(max_length=64)),
                ('expirydate', models.DateField()),
                ('description', models.TextField()),
                ('batchno', models.CharField(max_length=126)),
            ],
        ),
    ]
