# Generated by Django 3.0.6 on 2021-05-08 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machining', '0003_auto_20210507_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='tool',
            name='status',
            field=models.IntegerField(blank=True, choices=[(1, 'Active'), (2, 'Inactive')], default=1),
        ),
    ]