# Generated by Django 3.0.3 on 2020-02-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20200215_1755'),
        ('authentication', '0004_auto_20200215_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefprofile',
            name='specialities',
            field=models.ManyToManyField(blank=True, to='management.Speciality'),
        ),
    ]