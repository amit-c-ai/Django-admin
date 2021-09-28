# Generated by Django 3.2.7 on 2021-09-27 14:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_auto_20210927_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='country_field',
            new_name='Country_field',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='district',
            new_name='District',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='Name',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='population',
            new_name='Population',
        ),
        migrations.RenameField(
            model_name='city',
            old_name='state',
            new_name='State',
        ),
        migrations.AddField(
            model_name='city',
            name='Nationality',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.country'), max_length=30),
        ),
    ]
