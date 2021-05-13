# Generated by Django 3.2.2 on 2021-05-13 15:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tittle', models.CharField(max_length=100)),
                ('events_date', models.DateField()),
                ('events_time', models.DateTimeField()),
                ('location', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('cover', models.ImageField(upload_to='uploads/%Y/%m/%d')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
