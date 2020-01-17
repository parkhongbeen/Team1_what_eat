# Generated by Django 2.2.9 on 2020-01-17 06:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('category', models.CharField(max_length=50)),
                ('menu', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=300)),
                ('tel', models.CharField(max_length=30)),
                ('restaurant', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
