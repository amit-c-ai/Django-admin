# Generated by Django 3.2.7 on 2021-09-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20210927_2157'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='are_you_Student',
            field=models.BooleanField(default=False),
        ),
    ]
