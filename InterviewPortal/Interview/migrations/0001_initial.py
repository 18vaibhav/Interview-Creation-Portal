# Generated by Django 3.2.3 on 2021-12-19 06:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('participants', models.ManyToManyField(related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
