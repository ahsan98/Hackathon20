# Generated by Django 3.0.3 on 2020-02-15 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chefprofile',
            name='specialities',
            field=models.ManyToManyField(to='management.Speciality'),
        ),
    ]
