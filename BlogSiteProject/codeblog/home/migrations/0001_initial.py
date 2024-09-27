# Generated by Django 4.1.3 on 2024-09-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
