# Generated by Django 4.1.3 on 2024-09-27 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_contact_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
