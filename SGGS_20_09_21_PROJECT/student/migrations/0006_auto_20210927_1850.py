# Generated by Django 3.2.7 on 2021-09-27 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20210923_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='district',
            field=models.CharField(default='enter dist. here..', max_length=30),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.CharField(default='enter state here..', max_length=30),
        ),
    ]
