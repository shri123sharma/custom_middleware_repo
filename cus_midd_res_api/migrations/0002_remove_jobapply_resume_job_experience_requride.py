# Generated by Django 4.2 on 2023-04-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cus_midd_res_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapply',
            name='resume',
        ),
        migrations.AddField(
            model_name='job',
            name='experience_requride',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
