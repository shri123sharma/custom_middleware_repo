# Generated by Django 4.2 on 2023-04-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com_name', models.CharField(blank=True, max_length=255, null=True)),
                ('com_loaction', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
