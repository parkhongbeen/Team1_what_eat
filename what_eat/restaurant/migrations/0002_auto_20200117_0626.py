# Generated by Django 2.2.9 on 2020-01-17 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='restaurant',
            new_name='user',
        ),
    ]