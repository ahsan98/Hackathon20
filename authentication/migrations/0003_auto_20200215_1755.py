# Generated by Django 3.0.3 on 2020-02-15 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_chefprofile_specialities'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chefprofile',
            name='percentage',
            field=models.FloatField(null=True),
        ),
    ]
