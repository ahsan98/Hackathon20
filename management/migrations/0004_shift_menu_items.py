# Generated by Django 3.0.3 on 2020-02-15 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0003_auto_20200215_2145'),
        ('management', '0003_remove_kitchen_max_cooks'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='menu_items',
            field=models.ManyToManyField(blank=True, to='ordering.Item'),
        ),
    ]
