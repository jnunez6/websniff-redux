# Generated by Django 2.1.4 on 2020-03-25 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sniffapp', '0016_auto_20200322_1843'),
    ]

    operations = [
        migrations.AddField(
            model_name='gwcandidate',
            name='percentlikely',
            field=models.IntegerField(default=0),
        ),
    ]
